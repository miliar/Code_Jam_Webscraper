def solve(s):
    ok = False
    while not ok:
        for i in range(len(s)-1):
            if s[i] > s[i+1]:
                s[i] -= 1
                for j in range(i+1, len(s)):
                    s[j] = 9
                break
        ok = True
        for i in range(len(s)-1):
            ok &= s[i] <= s[i+1]
    return str(int(''.join(map(str, s))))

import sys
sys.stdin = open('in.txt')
sys.stdout = open('out.txt', 'w', encoding='ascii', newline='\n')
q=int(input())
for i in range(q):
    s = list(map(int,list(input())))
    print('Case #{:d}:'.format(i+1), solve(s))
sys.stdin.close()
sys.stdout.close()