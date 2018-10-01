import sys
import os

In = open(os.path.dirname(os.path.abspath(__file__))+'/'+sys.argv[1])
Out = open(os.path.dirname(os.path.abspath(__file__))+'/'+sys.argv[2],'w')

def flip(a):
    if a == '-':
        return '+'
    if a == '+':
        return '-'

if __name__ == '__main__':
    T = int(In.readline())
    for x in range(T):
        print(x+1)
        S, K = In.readline().rstrip('\n').split()
        K = int(K)
        print(S,K)
        out = 0
        tmp = list(S[0:K])
        for i in range(len(S)-K+1):
            if i == len(S)-K:
                if ''.join(tmp) == K*'-':
                    out += 1
                    break
                elif ''.join(tmp) == K*'+':
                    break
                else:
                    out = 'IMPOSSIBLE'
                    break
            if tmp[0] == '-':
                out += 1
                tmp = list(map(lambda x: flip(x), tmp[1:]))
                tmp.append(S[i+K])
                print('Case1',i,str(tmp))
            else:
                print(tmp[1:], S[i+K])
                tmp = tmp[1:]+[S[i+K]]
                print('Case2',i,str(tmp))
        Out.write('Case #{}: {}\n'.format(x+1,out))
