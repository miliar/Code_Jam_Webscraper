with open('A-large.in', 'r') as f:
    lines = f.readlines()
T = int(lines[0].strip())
lines = lines[1:T+1]

def flip(s):
    return ''.join(['+' if x == '-' else '-' for x in s])

g = open('A_large_output.txt', 'w')
    
for t, line in enumerate(lines):
    S, K = line.strip().split(' ')
    K = int(K)
    L = len(S)
    count = 0
    for i in range(L):
        if S[i] == '-':
            if i+K-1 < L:
                S = S[:i] + flip(S[i:i+K]) + S[i+K:]
                count += 1
            else:
                count = -1
                break
    g.write('Case #%d: ' % (t+1) + (str(count) if count != -1 else 'IMPOSSIBLE') + '\n')
                
g.close()
