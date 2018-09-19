def del_double(l):
    l = list(l)
    i = 0
    while i < len(l)-1:
        if l[i] == l[i+1]:
            l.pop(i)
        else:
            i += 1
    return l


def possible(l):
    pattern = del_double(l[0])
    p = True
    for s in l:
        if del_double(s) != pattern:
            p = False
    if p:
        return pattern
    else:
        return None

def nb_o(c,s):
    n = 0
    s = list(s)
    while 0 != len(s) and s[0] == c:
        n+=1
        s.pop(0)
    return n

t = int(raw_input())
for case in range(1,t+1):
    n = int(raw_input())
    l = []
    for i in range(n):
        l.append(list(raw_input()))

    if possible(l):
        pattern = list(del_double(l[0]))
        result = 0
        while(pattern != []):
            c = pattern[0]
            nb = [nb_o(c,s) for s in l]
            moy = sum(nb)//len(nb)
            result += sum(abs(n-moy) for n in nb)
            l = [l[i][nb[i]:] for i in range(len(l))]
            pattern.pop(0)
        print("Case #"+str(case)+": "+str(result))
    else:
        print("Case #"+str(case)+": "+"Fegla Won")


