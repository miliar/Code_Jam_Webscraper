
def calc(K, B, T, N, X, V):
    #for t in range(T+1):
    #    #print "time %d:" % t, 
    #    state = [X[i]+t*V[i] for i in range(N)]
    #    Goals = len([c for c in state if c >= B])
    
    final = [X[i]+T*V[i] for i in range(N)]
    Goals = len([c for c in final if c >= B])
    if Goals < K:
        return "IMPOSSIBLE"
    
    swaps = 0
    left = K
    final = final[::-1]
    for c in final:
        if left == 0:
            break
        if c >= B:
            left -= 1
        else:
            swaps += left
    return swaps


if __name__ == '__main__':
    C = int(raw_input())
    
    for c in range(C):
        N, K, B, T = map(int, raw_input().split())
        #print K, B
        X = map(int, raw_input().split())
        V = map(int, raw_input().split())
        
        print "Case #%d:" % (c+1), calc(K, B, T, N, X, V)
        