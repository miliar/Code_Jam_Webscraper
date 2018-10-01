import sys

def solve_case(sz, lst):
    needed = 0
    s = 0
    for i in range(sz+1):
        if s < i:
            needed = max(needed, i - s)
        s += lst[i]
    return needed

def main():
    filename = "A-large.in"
    f = open(filename)
    T = int(f.readline())
    for i in xrange(T):
        case = f.readline().split()
        result = solve_case(int(case[0]), map(int, list(case[1])))
        print "Case #%d: %d" % (i+1, result)

if __name__ == '__main__':
    main()

