def p(str):
    #print str
    pass

def al(str):
    l = []
    l2 = []
  
    lstr = len(str)
    for i in range(lstr):
        n = myatoi(str[i])
        l.append(n)
        if n not in l2:l2.append(n)
    
    max = len(l2) 
    p(max)
    p(l)
    p(l2)
    ans = 0
    pos = 1
    p("max")
    p(len(l2))
    if len(l2) > 1:
        a = l2[0]
        l2[0] = l2[1]
        l2[1] = a
    else:
        l2.insert(0,"0")
        max = 2
    l.reverse()
    for ll in l:
        ans += l2.index(ll) * pos
        p("pos %d: ans %d" %(pos,ans))
        pos *= max
    return ans


def myatoi(i):
    if i.isdigit():
        n = int(i)
    elif i.islower():
        n = ord(i)-ord('a')+10
    else:
        n = ord(i)-ord('A')+10

    p("%s,%d" %( i ,n))
    return n
p("ans:%d" % al("1111111"))
#p("ans:%d" % al("q9qh"))
#al("a")
#al("A")

