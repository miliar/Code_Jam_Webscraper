import sys

def can_have_p(total, p):
    if total%3 == 0:
        normbest = total/3
        surprisebest = total/3+1
    elif total%3 == 1:
        normbest = total/3+1
        surprisebest = total/3+1
    else:
        normbest = total/3+1
        surprisebest = total/3+2

    if total - normbest < 0: normbest = total
    if total - surprisebest < 0: surprisebest = total

    if normbest >= p: return 1, 0
    elif surprisebest >= p: return 1, 1
    else: return 0, 0

def test():
    fin = open('sample.in')

def main():
    fin = open(sys.argv[1])
    with open(sys.argv[2], 'wb') as fout:
        T = int(fin.readline())
        for icase in range(T):
            ints = [int(s) for s in fin.readline().strip().split()]
            N = ints[0]
            S = ints[1]
            p = ints[2]
            t = ints[3:]
            assert len(t) == N
            nhavep = 0
            for i in range(N):
                canhave, surprise = can_have_p(t[i], p)
                if canhave:
                    if not surprise:
                        nhavep += 1
                    else:
                        if S > 0:
                            nhavep += 1
                            S -= 1
            print >>fout, 'Case #%d: %d' % (icase+1, nhavep)
    fin.close()


if __name__ == '__main__':
    main()
