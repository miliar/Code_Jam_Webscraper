##from sys import stdin, stdout
with open ("C-small-1-attempt0.in.txt") as stdin, open("Coutnew.txt", 'w') as stdout:
    stdin.readline()
    for i, line in enumerate(stdin, start=1):
        stdout.write(f'Case #{i}: ')
        N, K = map(int, line.split())
        stalls=[0,N+1]
        for _ in range(K):
            diffs=[abs(x-y) for x,y in zip(stalls,stalls[1:])]
            ind = max(range(len(diffs)), key = lambda i: diffs[i])
            stalls.insert(ind+1, stalls[ind]+diffs[ind]//2)
        final = stalls[ind+1]
        a = abs(final-stalls[ind])-1
        b = abs(final - stalls[ind+2])-1
        
        stdout.write(f"{max(a,b)} {min(a,b)}\n")
