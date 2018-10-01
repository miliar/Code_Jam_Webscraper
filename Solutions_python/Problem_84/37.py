
import sys

def solve(case):
    (r,c) = map(int,raw_input().split())
    m=[]
    for i in range(r):
        m.append(list(raw_input()))

    for i in range(r):
        for j in range(c):
            if m[i][j] == '#':
                if (i == r-1) or (j == c-1) or (m[i+1][j] != '#') or (m[i][j+1] != '#') or (m[i+1][j+1] != '#'):
                    print "Case #%s:" % case
                    print "Impossible"
                    return
                else:
                    m[i][j] = '/'
                    m[i][j+1] = '\\'
                    m[i+1][j] = '\\'
                    m[i+1][j+1] = '/'
    
    print "Case #%s:" % case
    for i in range(r):
        for j in range(c):
            sys.stdout.write(m[i][j])
        sys.stdout.write('\n')
    sys.stdout.flush()
    

def main():
    t = int(raw_input())
    for i in range(t):
        solve(i+1)


main()
