import optparse

class CodeJamInputFile(object):
    
    def __init__(self, file_name, lines_per_case):
        self.file = open(file_name, 'r')
        self.lines_per_case = lines_per_case
        self.nof_cases = int(self.file.readline().strip("\n\r "))
        
    def __iter__(self):
        return self
    
    def next(self):
        lines = []
        for i in xrange(self.lines_per_case):
            line = self.file.readline()
            
            if len(line) == 0 and i == 0:
                raise StopIteration
            elif len(line) == 0:
                raise Exception("Input error")
            else:  
                lines.append(line.strip("\n\r "))
        
        return lines

def is_recycled(n, m):
    
    n = str(n)
    m = str(m)
    
    if n == m:
        raise Exception("n and m should not be equal")
    
    length = len(n)
    if length != len(m):
        return False
    
    if length == 1:
        return False
    
    for i in range(1, length):
        if n == m[-i:] + m[:-i]:
            return True
    
    return False


if __name__ == "__main__":
    
    parser = optparse.OptionParser()

    parser.add_option("-i", "--in-file", dest="input_file",
                      help="input file")

    (options, args) = parser.parse_args()

    input = CodeJamInputFile(options.input_file, 1)
    
    for ix, case in enumerate(input):
        items = case[0].split()
        start = int(items[0].strip())
        end = int(items[1].strip())
        
        if len(items) != 2:
            raise Exception("Invalid nof items")
        
        if end < start:
            raise Exception("End is less then start")
        
        nof_recycles = 0
        
        for n in range(start, end + 1):
            for m in range(n + 1, end + 1):
                 if is_recycled(n, m):
                     nof_recycles += 1
        
        print "Case #%d: %s" % (ix + 1, nof_recycles)
    



