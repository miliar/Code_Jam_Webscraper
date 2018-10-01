import math
def fair_and_square(a, b):
    num = 0
    left = int(math.sqrt(a))
    right = int(math.sqrt(b))
    for i in range(left, right+1):
        if i*i >=a and palindrome(i) and palindrome(i*i):
            num += 1
            #print(i*i)
    return num

def palindrome(x):
    s = str(x)
    l = len(s)
    for i in range(l//2):
        if s[i] != s[l-i-1]:
            return False
    return True
    
f = open('C-small-attempt0.in','r')
output = open('fairandsquare.txt','w')
lines = f.readline()
for i in range(int(lines)):
    lst = [int(x) for x in f.readline().split()]
    result = fair_and_square(lst[0], lst[1])
    output.write('Case #{0}: {1}\n'.format(i+1, result))
f.close()
output.close()
        

