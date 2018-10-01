# encoding: UTF-8
#Google Code Jam 2017 Round1B
#Problem B

import collections
import itertools
import sys

class gcj:
    identity = lambda x: x

    @classmethod
    def _read_line_raw(cls):
        line = in_file.readline()
        if not line:
            raise EOFError()
        return line.rstrip('\r\n')

    @classmethod
    # read single character
    def token(cls, conv=identity):
        line = cls._read_line_raw()
        return conv(line)

    @classmethod
    # read multiple single characters splitted by sep
    def tokens(cls, conv=identity, sep = ' '):
        line = cls._read_line_raw()
        return [conv(i) for i in line.split(sep)]

    current_case = 0

    @classmethod
    def case(cls):
        cls.current_case += 1
        return('Case #{}: '.format(cls.current_case))

def solve():
    N, R, O, Y, G, B, V = gcj.tokens(int)
    RR = R - G
    YY = Y - V
    BB = B - O
    print(RR,YY,BB)
    if RR <= 0:
        if (R==G) & (R+G == N):
            return('RG'*(N//2))
        elif not((R==0) & (G==0)):
            return('IMPOSSIBLE')
    if YY <= 0:
        if (Y==V) & (Y+V == N):
            return('YV'*(N//2))
        elif not((Y==0) & (V==0)):
            return('IMPOSSIBLE')
    if BB <= 0:
        if (B==O) & (B+O == N):
            return('BO'*(N//2))
        elif not((B==0) & (O==0)):
            return('IMPOSSIBLE')
    if 2 * max((RR,YY,BB)) > (RR+YY+BB):
        return('IMPOSSIBLE')
    RG = 'RG'*G + 'R'
    YV = 'YV'*V + 'Y'
    BO = 'BO'*O + 'B'

    s = [RR,YY,BB]
    ind = sorted(range(len(s)), key=lambda k: s[k])
    chlst = ['R','Y','B']
    ch2lst = [RG,YV,BO]
    ch = [chlst[i] for i in ind]
    ch2  = [ch2lst[i] for i in ind]
    s.sort()
    a,b,c = s
    ans = ''
    if (a-c+b)>0:
        ans += ch2[2]+ch2[0]+ch2[1]
        ans += (ch[2]+ch[0]+ch[1])*(a-c+b-1)
        ans += (ch[2]+ch[1])*(c-a)
        ans += (ch[2]+ch[0])*(c-b)
    elif (c-b)>0:
        # a!=0
        ans += ch2[2]+ch2[1]
        # ans += (ch[2]+ch[0]+ch[1])*(a-c+b)
        ans += (ch[2]+ch[1])*(c-a-1)
        ans += ch[2]+ch2[0]
        ans += (ch[2]+ch[0])*(c-b-1)
    else:
        # (c-b)=0, a=0
        ans += ch2[2]+ch2[1]
        # ans += (ch[2]+ch[0]+ch[1])*(a-c+b)
        ans += (ch[2]+ch[1])*(c-a-1)
        # ans += (ch[2]+ch[0])*(c-b)
    return(ans)




def main():
    sys.setrecursionlimit(9999)
    t = gcj.token(int)
    for _ in range(t):
        case = gcj.case()
        solution = solve()
        out_file.write(case+solution+"\n")
        print(case+solution)
        sys.stdout.flush()

problem_name = 'B-large'
in_file = open(problem_name+'.in',"r")
out_file = open(problem_name+'.out', "w")
main()
in_file.close()
out_file.close()