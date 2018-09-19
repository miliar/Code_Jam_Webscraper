"""
    Homebrewed Codejam framework
    
    Author: macduy
    Usage:
        
        codejam.py (py-source-file) (input-file) [> (output-file)]     << DEPRECATED >>
        codejam.py -r[gTo] (directory) (program) (input-file-name)
        codejam.py -t[T] (directory) (program)
        
        Add -g switch for input-file guessing. First match will be used
        Add -o for output to file. File name is automatically guessed and placed in directory
        Add -t for running on internal test cases. Input file will be ignored
        Add -T for timer output
        
        Use -x as shortcut for -rgTo
        
    Example:
        
        codejam.py B.py B-small.in >B-small.out
        codejam.py -rgo . B B-sm
        
    Source file formatting:
        Source file must contain INPUT and main(). OUTPUT and TEST are optional
"""

import sys, imp, inspect, os, time

# define custom data type to hold data
class Array(list):
    @property
    def range(self):
        return range(len(self))
        
    @property
    def length(self):
        return len(self)

def test():
    print "Code jam"
    
def guess_file(dir, filename, ext_c):
    for fn in os.listdir(dir):
        try:
            name, ext = fn.split('.')
            if ext == ext_c and name.find(filename) > -1:
                return name
        except:
            pass
                    
    raise Exception('No file match found')
    
    # returns a datatype processor function
def get_type_proc(type):
    if inspect.isfunction(type) or inspect.isclass(type):
        # if callable, use it
        return lambda x: type(x.rstrip('\n'))
    elif isinstance(type, tuple):
        return lambda x: map(lambda y,t: get_type_proc(t)(y), x.rstrip('\n').split(' '), type)
    else:
        return {
            'string' : lambda x: x.rstrip('\n'),
            'raw': lambda x: x,
            'int': int,
            'float': float
        }[type]

# returns a structure parser
def array_parser(next, type_proc, data):
    M = int(next())
    data = Array()
    
    for m in range(M):
        raw = next()
        data.append(type_proc(raw))
    return data

def multiarray_parser(next, type_proc, data):
    data = Array()
    conf = map(lambda x: int(x), next().split(' '))
    for c in conf:
        subdata = Array()
        for m in range(c):
            raw = next()
            subdata.append(type_proc(raw))
        data.append(subdata)
    return data

def internal_parser(next, type_proc, data, parser,length_f):
    M = length_f(data)
    data = Array()
    
    for m in range(M):
        data.append(parser(next, type_proc, data))
    return data
    
def get_struct_parser(struct):
    if inspect.isfunction(struct):
        return struct
    elif isinstance(struct, tuple):
        internal_struct, length_f = struct
        assert internal_struct in ['constant', 'linearray']
        # return an internal parser
        return lambda next, type_proc, data: internal_parser(next, type_proc, data, get_struct_parser(internal_struct), length_f)
    else:
        if struct == 'array':
            return array_parser
        elif struct == 'multiarray':
            return multiarray_parser
        elif struct == 'constant':
            return lambda next, type_proc, data: type_proc(next())
        elif struct == 'linearray':
            return lambda next, type_proc, data: Array(map(type_proc, next().rstrip('\n').split(' ')))
        else:
            raise Exception('Unknown struct')

            
def testcase_output(string, separator):
    n = 0
    splitter = ':' + separator
    string = string.partition(splitter)[2]
    while string:
        pre, sep, string = string.partition(splitter)
        expected, nl, garbage = pre.rpartition('\n')      
        
        n += 1
        yield n, expected


# Program begins here
def main():
    OUTFILE = None
    TEST = False
    TEST_FAILS = 0
    CLOCK = False
    took = 0.0
    total_time = 0.0

    if sys.argv[1][0] == '-':
        # switch syntax
        switch = sys.argv[1][1:]
        if switch.find('x') > -1:
            switch = "rgTo"
        if switch.find('r') > -1:
            dir, program_name, input_file = sys.argv[2:]
            if switch.find('g') > -1:
                input_file = guess_file(dir,input_file,'in')
            infile = ''.join([dir, '\\', input_file, '.in'])
            if switch.find('o') > -1:
                OUTFILE = open(''.join([dir, '\\', input_file, '.out']), 'w')
        elif switch.find('t') > -1:
            TEST = True
            dir, program_name = sys.argv[2:]
        else:
            raise Exception('Uknown syntax')
            
        source = ''.join([dir, '\\', program_name, '.py'])
        if switch.find('T') > -1:
            CLOCK = True
            
        # use a safer method of import
        sys.path.append(''.join([os.path.abspath(os.path.dirname(__file__)),'\\',dir]))
        program = __import__(program_name)
    else:
        # default format
        source, infile = sys.argv[1], sys.argv[2]
        # load program from filename
        program = imp.load_source('module.name', source)
    
    # load output string if available
    try:
        OUTPUT = program.OUTPUT
    except:
        OUTPUT = None

    # determine separator
    try:
        SEPARATOR = program.SEPARATOR
    except:
        SEPARATOR = " "
    
    # open file
    if not TEST:
        f = open(infile, 'r')
        next = f.readline
    else:
        tc_input, tc_output = program.TEST
        next = iter(tc_input.split('\n')).next
        next_output = iter(testcase_output(tc_output, SEPARATOR)).next
        
    # process input
    type_procs = []
    struct_parsers = []
    
    try:
        INPUT_ORDER = program.INPUT_ORDER
    except:
        INPUT_ORDER = program.INPUT.keys()
    VARIABLES_RANGE = range(len(INPUT_ORDER))
        
    for var_name in INPUT_ORDER:
        # read information
        type, struct = program.INPUT[var_name]
        # choose data processor function
        type_procs.append(get_type_proc(type))
        # choose structure parser
        struct_parsers.append(get_struct_parser(struct))

    # process header
    try:
        HEADER = program.HEADER
        try:
            HEADER_ORDER = program.HEADER_ORDER
        except:
            HEADER_ORDER = program.HEADER.keys()
    except:
        HEADER = {'_test_cases_': ('int', 'constant')}
        HEADER_ORDER = ['_test_cases_']
    
    header_data = dict()    
    for header_var_name in HEADER_ORDER:
        type, struct = HEADER[header_var_name]
        header_data[header_var_name] = get_struct_parser(struct)(next, get_type_proc(type), header_data)
    
    # determine number of cases
    try:
        N = program.TEST_CASES(header_data)
    except:
        N = header_data['_test_cases_']
        del header_data['_test_cases_']
        
    # pass header data
    try:
        program.header(**header_data)
    except:
        pass
    
    # process each test case - Main Loop    
    for n in range(N):
        # load input data
        kw = dict()
        
        for i in VARIABLES_RANGE:
            kw[INPUT_ORDER[i]] = struct_parsers[i](next, type_procs[i], kw)
            
        start = time.clock()
        result = program.main(**kw)
        took = time.clock() - start

        
        # present results
        total_time += took
        if not OUTPUT:
            # infer from result
            types = []
            if not isinstance(result, tuple):
                result = tuple([result])
            for x in result:
                if isinstance(x, int):
                    types.append('%i')
                elif isinstance(x, str):
                    types.append('%s')
                elif isinstance(x, float):
                    types.append('%f')
            OUTPUT = ' '.join(types)
            
        result_output = (OUTPUT % result)
            
        if not (OUTFILE or TEST) or CLOCK:
            # standard output
            if not TEST:
                print "Case #%i:%s%s" % (n+1, SEPARATOR, result_output),
                if CLOCK:
                    print "(%fs)" % (took),
                print ""
        if TEST or OUTFILE:
            out = "Case #%i:%s%s" % (n+1, SEPARATOR, result_output)
            if TEST:
                # check against file's internal test
                print "Case #%i:" % (n+1),
                test_n, expected = next_output()
                if result_output != expected:
                    TEST_FAILS += 1
                    print "fail",
                    if CLOCK:
                        print "(%fs)" % (took),
                    print ""
                    print "Expected:%s%s" % (SEPARATOR, expected)
                    print "Got\t:%s%s" % (SEPARATOR, result_output)
                else:
                    print "pass",
                    if CLOCK:
                        print "(%fs)" % (took),
                    
                    print ""
            else:
                # output to file
                OUTFILE.write(out)
                OUTFILE.write('\n')

    if OUTFILE:
        OUTFILE.close()
    if TEST:
        if TEST_FAILS == 0:
            print "Correct!"
        else:
            print "%i out of %i failed" % (TEST_FAILS, N)
    if CLOCK:
        print "Total time: %fs" % (total_time)
        
# end of main
        
if __name__ == "__main__":
    main()

# Set of useful 

class memoize:
    """ Function result memoization. Use as decorator """
    def __init__(self, function):
        self.function = function
        self.memoized = {}

    def __call__(self, *args):
        try:
            return self.memoized[args]
        except KeyError:
            self.memoized[args] = self.function(*args)
            return self.memoized[args]
            