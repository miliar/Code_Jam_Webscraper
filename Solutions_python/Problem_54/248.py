
def gcd(a,b):   #a > b
    if a < b:
        t = a
        a = b
        b = t
    if b == 0:
        return a
    return gcd(b,a % b)

if __name__ == '__main__':
    f = open('in.txt','r')
    fout = open('out.txt','w')
    n = int(f.readline())
    for test in range(0,n):
       buf = f.readline().split(' ')
       l = list()
       for i in range(1,len(buf)):
           l.append(long(buf[i]))
       l = set(l)
       l = list(l)
       s = set()
       for i in range(0,len(l)):
           for j in range(i+1,len(l)):
               s.add(abs(l[i] - l[j]))
       T = list(s)[0]
       for now in list(s):
           T = gcd(T,now)
       y = (T - ( l[0] % T ))
       if T == y:
           y = 0
       for i in range(1,len(l)):
           if y != T - (l[i] % T):
               y = 0
               break
       fout.write('Case #' + str(test+1) +': ' + str(y) + '\n')
       