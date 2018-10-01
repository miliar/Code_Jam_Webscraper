import sys
import math
import heapq
import pprint
import itertools
eps = 1e-6

def is_sorted(l):
    return all(a <= b for a, b in itertools.izip(l[:-1], l[1:]))

def digits_to_num(digits):
    return sum(d * 10**(len(digits) - i - 1) for i, d in enumerate(digits))

def main(infile, outfile):

    with open(infile) as inf:
        with open(outfile, 'w') as outf:
            test_case = 1
            t = int(inf.readline())
                
            while True:
                
                D, N = list(map(float, inf.readline().split()))
                # print("N: {} P: {}".format(N, P))
                h = []
                for i in range(int(N)):
                    h.append(tuple(map(float, inf.readline().split())))

                print(h)

                times = []
                for i, (di, si) in enumerate(reversed(h)):
                    times.append((D - di) / si)

                times_for_annie = max(times)
                annie_cruise = D / times_for_annie

                print('Case #{}: {}'.format(test_case, annie_cruise))
                outf.write('Case #{}: {}'.format(test_case, annie_cruise))
                if t != test_case:
                    outf.write('\n')
                else:
                    break
                test_case += 1

if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = sys.argv[2]

    main(infile, outfile)
