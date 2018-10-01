import sys
T = int(sys.stdin.readline().strip())

for t in range(1, T+1):
    n = [int(i) for i in sys.stdin.readline().strip()]
    same = 0
    found = False
    for i in range(1, len(n)):
        if n[i] > n[same]:
            same = i
        elif n[i] < n[same]:
            n[same] -= 1
            found = True
            break
    if found:
        for i in range(same+1, len(n)):
            n[i] = 9
    print('Case #{}: {}'.format(t, int(''.join([str(o) for o in n]))))

            
         
