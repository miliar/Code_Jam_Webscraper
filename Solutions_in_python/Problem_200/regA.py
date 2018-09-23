import sys
import math
import itertools


def is_sorted(l):
    return all(a <= b for a, b in itertools.izip(l[:-1], l[1:]))

def tidy(n):
    return is_sorted([])


def digits_to_num(digits):
    return sum(d * 10**(len(digits) - i - 1) for i, d in enumerate(digits))

def main(infile, outfile):

    with open(infile) as inf:
        with open(outfile, 'w') as outf:
            test_case = 1
            t = int(inf.readline())
            for line in inf.readlines():
                N = int(line)
                print "TC = {} LC = {}".format(test_case, N)
                chk = N
                while True:
                    # print "Checking", chk
                    digits = [int(k) for k in str(chk)]
                    # print "Ints", digits
                    for i, (a, b) in enumerate(itertools.izip(digits[:-1], digits[1:])):
                        if a > b:
                            digits[i] -= 1
                            for r in range(i+1, len(digits)):
                                digits[r] = 9
                            chk_n = digits_to_num(digits) 
                            # print 'sum', chk_n
                            assert chk != chk_n
                            chk = chk_n
                            break
                    
                    if is_sorted(digits):
                        
                        print "Case #{}: {}".format(test_case, chk)
                        outf.write("Case #{}: {}".format(test_case, chk))
                        break

                if t != test_case:
                    outf.write('\n')
                test_case += 1

if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = sys.argv[2]

    main(infile, outfile)
