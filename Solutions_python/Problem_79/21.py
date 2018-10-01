from sys import stdin
buf = []
for line in stdin:
    buf.insert(0, line.strip())

def cond(a, letter):
    return [i for i in range(len(a)) if a[i] == letter]

def solv(dic, lis):
    n = len(dic)
    loss = [0 for i in range(n)]
    S = []
    for i in range(n):
        for s in S:
            if len(dic[i]) == len(dic[s[0]]):
                s.append(i)
                break
        else:
            S.append([i])
#    print S
    for letter in lis:
        Sp = []
        for s in S:
            # calc part(s)
            ps = []
            for e in s:
                for pse in ps:
                    if cond(dic[e], letter) == cond(dic[pse[0]], letter):
                        pse.append(e)
                        break
                else:
                    ps.append([e])
            if len(ps) != 1:
                for pse in ps:
                    condi = cond(dic[pse[0]], letter)
                    if condi:
                        continue
                    for i in pse:
                        loss[i] += 1
            Sp.extend(ps)
        S = Sp
    ml = max(loss)
    for i in range(n):
        if ml == loss[i]:
            return i
    return n

def solve(dic, lis):
    return ' '.join(dic[solv(dic, l)] for l in lis)

T = int(buf.pop())
for t in range(1, T+1):
    prob = [int(e) for e in buf.pop().split()]
    dic = []
    lis = []
    for i in range(prob[0]):
        dic.append(buf.pop())
    for i in range(prob[1]):
        lis.append(buf.pop())
    ans = solve(dic, lis)
    print 'Case #' + str(t) + ': ' + ans
