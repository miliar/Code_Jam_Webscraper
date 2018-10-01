import sys

def flip(S,st,ed):
    #print("flip: ", S, st, ed)
    r = list(S);
    for i in range(st,ed):
        if (S[i]=='-'):
            r[i]='+'
        else:
            r[i]='-'
    result="".join(r)
    #print("flip done: ", result)
    return result


def pancake(S,K):
    cnt=0
    for i in range(len(S)):
        if (S[i]=='-'):
            if (i+K<=len(S)):
                S = flip(S,i,i+K)
                cnt+=1
            else:
                return -1
    return cnt

if __name__=='__main__':
    T = int(sys.stdin.readline())
    for i in range(T):
        (S,K) = sys.stdin.readline().split(' ')
        result = pancake(S,int(K))
        if (result>=0):
            print ("Case #%d: %d"%(i+1, result))
        else:
            print ("Case #%d: IMPOSSIBLE"%(i+1))

