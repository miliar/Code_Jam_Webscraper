import random
import sys

def write_large_test(filename):
    f = open(filename, 'w')
    f.write('100\n')
    for _ in range(100):
        f.write(generate_test_case(100)+'\n')
    f.close()

def write_small_test(filename):
    f = open(filename, 'w')
    f.write('20\n')
    for _ in range(20):
        f.write(generate_test_case(10)+'\n')
    f.close()

def generate_test_case(steps_max):
    steps = random.randint(1, steps_max)
    result = str(steps)
    for _ in range(steps):
        result += ' %s %s' % (random.choice(('O','B')), random.randint(1, 100))

    return result

def parse_test_case(line):
    steps = []
    case = line.split()
    for s in xrange(1, (int(case[0]))*2, 2):
        steps.append((case[s], int(case[s+1].strip())))

    return steps

def run_test_case(steps):
    turns = []
    o = []
    b = []
    lasto=1
    lastb=1
    for s in steps:
        turns.append(s[0])
        if s[0]=='O':
            o.append(max(lasto, s[1]) - min(lasto, s[1])+1)
            lasto = s[1]
        else:
            b.append(max(lastb, s[1]) - min(lastb, s[1])+1)
            lastb = s[1]

    total = 0
    oindex = 0
    bindex = 0
    owork = 0
    bwork = 0
    for t in turns:
        if t=='O':
            change = o[oindex]
            if bwork:
                change = change - min(o[oindex]-1, bwork) # -1 for the button press
            total = total + change
            owork = owork + change
            oindex += 1
            bwork = 0
        elif t=='B':
            change = b[bindex]
            if owork:
                change = change - min(b[bindex]-1, owork) # -1 for the button press
            total = total + change
            bwork = bwork + change
            bindex += 1
            owork = 0

    return total


if __name__=='__main__':
    f = open(sys.argv[1], 'r')
    num_test_cases = int(f.readline())
    for i in range(num_test_cases):
        test_case = parse_test_case(f.readline())
        v = run_test_case(test_case)
        print 'Case #%d: %s' % (i+1, v)
    f.close()