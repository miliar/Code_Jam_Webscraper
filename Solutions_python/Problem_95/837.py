
def read_input(filename):
    data = []
    with file(filename, 'rt') as f:
        for line in f:
            data.append(line)
        
    line_num = int(data[0].strip())
    lines = [data[i].strip() for i in xrange(line_num + 1)]
    lines = lines[1:]
    print lines
    #assert len(lines) == line_num
    
    return lines

def get_translation(lines):
    d = {'a': 'y',
         'b': 'h',
         'c': 'e',
         'd': 's',
         'e': 'o',
         'f': 'c',
         'g': 'v',
         'h': 'x',
         'i': 'd',
         'j': 'u',
         'k': 'i',
         'l': 'g',
         'm': 'l',
         'n': 'b',
         'o': 'k',
         'p': 'r',
         'q': 'z',
         'r': 't',
         's': 'n',
         't': 'w',
         'u': 'j',
         'v': 'p',
         'w': 'f',
         'x': 'm',
         'y': 'a',
         'z': 'q',
         ' ': ' '}
    
    new_lines = []
    for line in lines:
        new_str = ''
        for let in line:
            new_str += d[let]
            
        new_lines.append(new_str)
        
    return new_lines

def create_output(translation):
    with file('output1.txt', 'wt') as f:
        for (i, line) in enumerate(translation):
            print >> f, 'Case #%d: %s' % (i + 1, line) 
            
def main():
    import sys
    data = read_input(sys.argv[1])
    translation = get_translation(data)
    create_output(translation)

if __name__ == "__main__":
    main()