HOMEDIR = '' # 'C://Users/srulix/Downloads/GCJ/'

def cjwrap(answerer, input_filename):
    fin = file(HOMEDIR + input_filename, 'r')
    output_filename = input_filename.replace('.in', '.out')
    fout = file(HOMEDIR + output_filename, 'w')
    inputs = int(fin.readline())
    for i in xrange(inputs):
        output = answerer(fin)
        fout.write("Case #%s: %s\n" % (i+1, str(output)))
    fout.close()

def make_ints(line):
    return [int(x) for x in line.split()]
    
def single_line_answer(f):
    return process(f.readline())

def process(line):
    return line