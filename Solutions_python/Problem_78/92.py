import sys
filein, fileout = sys.argv[1:3]

def gcd(a,b):
    return a if b == 0 else gcd(b, a%b)

def solve(n, pd, pg):
    return "Possible" if (pg != 100 or pd == 100) and (pg != 0 or pd == 0) and 100/gcd(100,pd) <= n else "Broken"

if __name__ == '__main__':
    with open(filein, 'rU') as f1, open(fileout, 'w') as f2:
        T = int(f1.readline())
        for case in range(T):
            n, pd, pg = [int(x) for x in f1.readline().strip().split()]
            f2.write("Case #{}: {}\n".format(case+1, solve(n, pd, pg)))

