
def solve(S,K):
    S = list(S)
    try:
        i = S.index('-')
    except ValueError:
        return 0
        
    count = 0
    while i >= 0:
        if i > len(S) - K:
            return "IMPOSSIBLE"
        for j in range(K):
            if S[i+j] == '-':
                S[i+j] = '+'
            else:
                S[i+j] = '-'
        count += 1
        try:
            i = S[i:].index('-') + i
        except ValueError:
            break
    return count
    
out = open('pancake_output.txt', 'w')
with open('A-small-attempt0.in') as f:
    T = int(f.readline().strip())
    for case_num in range(T):
        S,K = f.readline().strip().split()
        K = int(K)
        ans = solve(S,K)
        out.write("Case #%d: %s\n"%(case_num+1,ans))
out.close()    