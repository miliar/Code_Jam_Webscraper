from sys import stdin

def solve():
    T = int(stdin.readline())
    for casenum in range(T):
        l = [int(x) for x in stdin.readline().split()]
        r = solve_case(l[0], l[1], l[2], l[3:])
        print 'Case #%d: %d' % (casenum + 1, r)


def solve_case(n, s, p, t):
    r = 0
    for sum in t:
        if sum % 3 == 0:
            b1 = sum / 3
            b2 = sum / 3 + 1 if (sum > 0 and sum < 30) else b1
        elif sum % 3 == 1:
            b1 = (sum - 1) / 3 + 1
            b2 = b1
        else:
            b1 = (sum - 2) / 3 + 1
            b2 = (sum - 2) / 3 + 2 if (sum < 29) else b1
        
        if b1 >= p:
            r += 1
        elif b2 >= p and s > 0:
            r += 1
            s -= 1
    
    return r

 
if __name__ == '__main__':
    solve()