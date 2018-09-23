f = open('Google Tidy Numbers Large.in','r')
g = open('Google Tidy Numbers Large.out','w')

def Google_print(filename,answers):
    for i in range(len(answers)):
        filename.write("Case #%s: %s\n" % (str(i+1),answers[i]))
        print "Case #%s: %s" % (str(i+1),answers[i])
    return

def is_tidy(n):
    s = list(str(n))
    s.sort()
    s = ''.join(s)
    if int(s) == n:
        return True
    return False

def first_off(s):
    prev = s[0]
    for i in range(1,len(s)):
        if s[i] < prev:
            return i
        prev = s[i]
    return None

def closest_tidy(s):
    L = len(s)
    if L in [0,1]:
        return s
    a = list(s)
    x = first_off(a)
    if not x:
        return s
    digit = a[x]
    for i in range(x,L):
        a[i] = '9'
    d2 = a[x-1]
    if d2 == '1':
        a = ['9']*(L-1)
        return ''.join(a)
    else:
        d2 = str(int(d2)-1)
        a[x-1] = d2
        tail = ''.join(a[x:])
        head = closest_tidy(''.join(a[:x]))
    return head+tail

#q = []
#for i in range(56789,66789):
    #if is_tidy(i):
        #q.append(i)
    #else:
        #v = int(closest_tidy(str(i)))
        #if v != q[-1]:
            #print i,q[-1],v
        
cases = int(f.readline())
answers = []
for i in xrange(cases):
    s = f.readline().rstrip()
    answers.append(closest_tidy(s))
Google_print(g,answers)
f.close()
g.close()
        
            
    
    


    