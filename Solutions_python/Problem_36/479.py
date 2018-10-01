
f = open('C-small-attempt1.in', 'r')

f.readline()
 
inpoot = []

for i in f:
     inpoot.append(i)
       
def func(n,w):

    result = 0

    if n == '':
        return 1

    s = n[0]
    w2 = w
    z = w2.find(s)

    while z != -1:
        result += func(n[1:],w2[(z+1):])
        w2 = w2[(z+1):]
        z = w2.find(s)
        

    return result

j = 1;

for a in inpoot:
     s= str(func('welcome to code jam',a ))

     zero = ''
     
     for i in range (4-len(s)):
         zero += '0';
         
     s = zero + s;
     print ('Case #' + str(j) + ': ' + s)
     j += 1
