import sys

def process(in_file):
    in_line = in_file.readline().strip().split(' ')[1:]

    buts = []
    for x in range(len(in_line)/2):
        buts.append([in_line[x*2], int(in_line[x*2+1])])


    O = 1
    B = 1
    T = 0
    next_O = True
    next_B = True
    T_O = T_B = 0

    while len(buts) > 0:
        if next_O is not False:
            next_O=False
            for x in buts:
                if 'O' in x:
                    next_O = x[1]
                    break
            if O == next_O and 'O' in buts[0]:
                T_O = 1 # Push
            elif O == next_O:
                T_O = 0 # Wait
            elif O is not False:
                T_O = abs(O - next_O)+1

        if next_B is not False:
            next_B=False
            for x in buts:
                if 'B' in x:
                    next_B = x[1]
                    break
            if B == next_B and 'B' in buts[0]:
                T_B = 1 # Push
            elif B == next_B:
                T_B = 0 # Wait
            elif B is not False:
                T_B = abs(B - next_B)+1

        if buts[0][0] == 'O':
            T+= T_O
            O = next_O
            if next_B is not False:
                if T_O>=T_B:
                    B=next_B
                else:
                    B = next_B - abs(next_B - B) + T_O
        else:
            T+= T_B
            B = next_B
            if next_O is not False:
                if T_B>=T_O:
                    O=next_O
                else:
                    O = next_O - abs(next_O - O) + T_B

        buts.pop(0)

    return str(T)

    


def main():
    if len(sys.argv) is not 2:
        print 'Pass in_file'
        return 1

    in_file = open(sys.argv[1], 'r')

    iterations = int(in_file.readline())

    for i in range(iterations):
        sys.stdout.write('Case #%d: %s\n' % (i+1, process(in_file)))

    
    in_file.close()
    sys.stdout.flush()

    return 0

if __name__ == '__main__':
    sys.exit(main())

