
def readint(f_in): return int(f_in.readline()[:-1])
def readfloat(f_in): return float(f_in.readline()[:-1])
def read_l(f_in): return f_in.readline()[:-1].split(' ')
def readint_l(f_in): return map(long,f_in.readline()[:-1].split(' '))
def readfloat_l(f_in): return map(float,f_in.readline()[:-1].split(' '))
def readchar_l(f_in): return list(f_in.readline()[:-1])
def plus_min_str_to10_l(str): return map(int,list(str.replace('+','1').replace('-','0')))
def list_to_str(out_list): return ' '.join(map(str,out_list))
imp="IMPOSSIBLE"

f_in=open('B-large.in','r')
f_out=open('out_large.txt','w')
output=""
T=readint(f_in)
import numpy as np

for i in range (T):
    output+="Case #"+str(i+1)+": "
    N, R, O, Y, G, B, V = readint_l(f_in)
    if O > B or G > R or V > Y:
        output += imp
    else:
        B -= O
        R -= G
        Y -= V
        if np.any(np.array([B,Y,R]) > (B+Y+R)/2.):
            output += imp
        else:
            res = ''
            [a,b,c] = [R, 'R'], [B,'B'], [Y,'Y']
            [a,b,c] = sorted([a,b,c], key=lambda x:x[0], reverse=True)
            d = b[0]-c[0]
            res += (a[1]+b[1])*d
            a[0] -= d
            b[0] -= d
            d = a[0]-b[0]
            res += (a[1]+b[1]+a[1]+c[1])*d
            a[0] -= d*2
            b[0] -= d
            c[0] -= d
            res += (a[1]+b[1]+c[1])*a[0]

            res = res.replace('B','B'+'OB'*O, 1)
            res = res.replace('R','R'+'GR'*G, 1)
            res = res.replace('Y','Y'+'VY'*V, 1)
            
            if 'B' not in res and O>0:
                if len(res)==0:
                    res = 'BO'*O
                else:
                    res = imp
                    
            if 'R' not in res and G>0:
                if len(res)==0:
                    res = 'GR'*G
                else:
                    res = imp
                    
            if 'Y' not in res and V>0:
                if len(res)==0:
                    res = 'VY'*V
                else:
                    res = imp
                    
            output += res
    output+="\n"

f_out.write(output)
print output
f_out.close()
f_in.close()
