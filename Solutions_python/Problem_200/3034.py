import argparse
import os


def output(out, case, line):
    num  = str(int(''.join(map(str, line))))
    print 'Case #%d:' % (case + 1), num
    out.write('Case #' + str((case + 1)) + ': ' + num + '\n')
    

def find_untidy(arr):
    if len(arr) > 1:
        for i in xrange(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                return i
    return -1


def solve(case, line, out):
    line = map(int, line)
    
    untidy = find_untidy(line)
    if untidy == -1:
        output(out, case, line)
        return
    else:
        for i in xrange(untidy + 2, len(line)):
            line[i] = 9
        while untidy >= 0 and line[untidy] > line[untidy + 1]:
            if line[untidy] > 0:
                line[untidy] -= 1
            line[untidy + 1] = 9
            untidy -= 1
    output(out, case, line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solve google codejam.')
    parser.add_argument('input', type=str, help='Input file')
    args = parser.parse_args()
    
    if os.path.isfile(args.input):
        file_name, ext = os.path.splitext(args.input)
        output_path = file_name + '.out'
        print args.input, ' => ', output_path
        
        with open(args.input) as inp:
            with open(output_path, 'w') as out:
                # Skip first line
                next(inp)
                
                for case, line in enumerate(inp):
                    solve(case, line.strip(), out)
                
    else:
        print "Input file does not exist"