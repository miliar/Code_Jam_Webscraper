def check(S):
    for i in S:
        if i == '-':
            return False
    return True        

def change(k,S,K):
    for i in range(K):
        if S[i+k] == '-':
            S[i+k] = '+'
        else:
            S[i+k] = '-'
              
def flip(S,K):
    count = 0
    for i in range(len(S)-K+1):
        if S[i] == '-':
            count += 1
            change(i,S,K)
    if check(S):
        return count
    else:
        return "IMPOSSIBLE"
      
T = int(input())
for i in range(T):
    SK = input().split(' ')
    s = SK[0]
    S = []
    for j in s:
        S.append(j)
    K = int(SK[1])
    c = flip(S,K)
    print("Case #"+str(i+1)+': '+str(c))
