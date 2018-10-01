import math
def palindrome(s):
    if(len(s)==0 or len(s)==1):
        return 1
    elif(s[0]==s[-1]):
        return palindrome(s[1:-1])
    else:
        return 0


inp = open('input.in','r')
out = open('output.out','w')
n = [int(x) for x in inp.readline().split()]
for j in range(n[0]):
    c=0
    a, b = [int(x) for x in inp.readline().split()]
    m,n=math.ceil(math.sqrt(a)), int(math.sqrt(b))+1
    for i in range(m,n ):
        s=str(i);
        ss=str(i*i);
        if(palindrome(s)==1 and palindrome(ss)==1):
            c=c+1
    out.write('Case #')
    out.write(str(j+1))
    out.write(': ')
    out.write(str (c))
    out.write('\n')
