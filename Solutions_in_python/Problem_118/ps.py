
import math
def closest(i):


    if "".join(i) == "".join(i)[::-1]:
        #print i
        return ("".join(i))
    else:
        n = len(i)
        i = list(i)
        q = 0
        w = n-1
        if q < w:            
            s = int(i[q])
            e = int(i[w])
            num = 0
            if s > e:
                i[w] = i[q]
                rest = closest(i[1:n-1])
                num =  (i[q] + str(rest) + i[w])
            elif s < e:
                i[q] = str(int(i[q])+1)
                i[w] = i[q]
                q+=1
                w-=1
                while q <= w:
                    i[q] = '0'
                    i[w] = '0'
                    q += 1
                    w -= 1
                num = ("".join(i))
            else:
                num =  (i[q] + str(closest(i[1:n-1])) + i[w])

        return num



def next_num(i):
    n = len(i)
    i = list(i)
    if n % 2 == 0:
        m = n / 2
        p = m - 1

        while True:
            if p < 0:
                return long("",join(i))+2
            m_s = i[m]
            p_s = i[p]             
            if p_s == '9':
                p-=1
                m+=1

            else:
                i[p] = str(int(i[p])+1)
                i[m] = i[p]
                break
    else:
        m = n/2
        m_s = i[m]
        if m_s != '9':
            i[m] = str(int(i[m])+1)
        else:
            p = m-1
            m = m+1
            while True:
                if p < 0:
                    return long("".join(i))+2
                m_s = i[m]
                p_s = i[p]             
                if p_s == '9':
                    p-=1
                    m+=1

                else:
                    i[p] = str(int(i[p])+1)
                    i[m] = i[p]
                    break


    return "".join(i)


def count(s,e):
    max_sqrt_e = int(math.floor(math.sqrt(e)))
    max_sqrt_c = int(math.ceil(math.sqrt(s)))
    i = max_sqrt_c
    i = long(closest(str(i)))
    count = 0
    while i <= max_sqrt_e:
        j = str(i)
        ne = long(next_num(j))
        if j == j[::-1]:
            n = i*i            
            l = str(n)
            if l == l[::-1]:
                count+=1
        i = ne
                
    return count

        
      

n = raw_input()
n = int(n)
for i in range(n):
    l = raw_input()
    toks = l.split()
    s = long(toks[0])
    e = long(toks[1])
    print "Case #%d: %d" % (i+1, count(s, e))
    

