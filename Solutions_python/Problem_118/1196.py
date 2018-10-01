import math




def is_palindrome(i):
    return (str(i) == str(i)[::-1])
    
def gen(a,b):
    palindromes=((x,is_palindrome(x)) for x in range(a,b+1))
    for (i,ispalindrome) in palindromes:
        if is_palindrome(i*i) and ispalindrome:
            yield i*i
with open('C-small-attempt1.in','r') as f:
    o = open('C-small.out','w')
    for z in range(int(f.readline())):
        line=f.readline().split()
        a,b=int(line[0]),int(line[1])
        count=0
        for i in gen(math.ceil(math.sqrt(a)),math.floor(math.sqrt(b))):
            count+=1
        o.write('Case #'+str(z+1)+': '+str(count)+'\n')
    o.close()
