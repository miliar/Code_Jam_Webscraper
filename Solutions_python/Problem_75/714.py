import sys
import getopt

def solve_case(num, line):
    parts = line.split(' ')

    num_combos = int(parts[0])
    num_oppos = int(parts[num_combos+1])
    spell = parts[-1]
    
    combos = {}
    oppos = []
    answer = []

    if num_combos > 0:
        for i in range(1, num_combos+1):
            combo = parts[i]
            combos[combo[:2]] = combo[-1]

    if num_oppos > 0:
        for i in range(num_combos+2, num_combos+2+num_oppos):
            oppo = parts[i]
            oppos.append(oppo)

    for c in spell:
        if c == '\n':
            break

        if len(answer) > 0:
            prev_c = answer[-1]
        else:
            prev_c = ''
            
        found_combo = False
        for pair in combos:
            if c in pair:
                other = pair.replace(c, '')

                # Pair of the same letter:
                if other == '':
                    other = c

                if other == prev_c:
                    answer.pop()
                    answer.append(combos[pair])
                    found_combo = True
                    break
        if found_combo:
            continue

        found_oppo = False
        for pair in oppos:
            if c in pair:
                other = pair.replace(c, '')
                if other in answer:
                    found_oppo = True
                    break

        if found_oppo:
            answer = []
        else:
            answer.append(c)

    answer = '[' + ', '.join(answer) + ']'

    return 'Case #%d: %s\n' % (num+1, answer)

def solve(argv):
    file = argv[1]
    with open(file, 'r') as f:
        lines = f.readlines()

    with open('b.out', 'w') as f:
        N = int(lines[0])
        
        for testcase, i in enumerate(range(1, N+1, 1)):
            out = solve_case(testcase, lines[i])
            f.write(out)

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv

    try:
        try:
            opts, args = getopt.getopt(argv[1:], 'h', ['help'])
        except getopt.error, msg:
            raise Usage(msg)
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, 'for help use --help'
        return 2

    solve(argv)

if __name__ == '__main__':
    sys.exit(main())
