__author__ = 'Janek Krukowski'

def solve_case(scores, snum, pnum):
    ret = 0
    sup = 0
    for n in scores:
        if 3*pnum <= n:
            ret += 1
            continue

        s = n - pnum
        if s < 0:
            continue
        m = s % 2
        k = s / 2
        triplet = (pnum, k+m, k)

        mx = max(triplet)
        mn = min(triplet)
        if mx > mn + 2:
            continue

        if mx == mn + 2:
            sup += 1
        else:
            ret += 1

    return ret + min(sup, snum)






def main():

    with open('B-large.in', 'r') as input, open('output.out', 'w') as output:
        cases = int(input.readline())
        for i in xrange(cases):
            line = input.readline().split(' ')
            gnum = int(line[0])
            snum = int(line[1])
            pnum = int(line[2])
            scores = [int(n) for n in line[3:]]
            output.write('Case #{0}: {1}\n'.format(i+1, solve_case(scores, snum, pnum)))





if __name__ == '__main__':
    main()

