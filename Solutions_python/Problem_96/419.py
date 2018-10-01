fout = open('dancing.txt', 'w')
fin = open('B-large.in', 'r')

def numb(t, S, p):
    if p == 0:
        return len(t)
    if p == 1:
        return len(t) - t.count(0)        
    good = p*3 - 2
    enoughgood = p*3 - 4
    ans = 0
    maybe = 0
    for x in t:
        if x >= good:
            ans += 1
        elif x >= enoughgood:
            maybe += 1
    ans += min(maybe, S)
    return ans
        

T = int(fin.readline())
for i in range(T):
    print i
    s = fin.readline()
    temp = map(int, s.split())
    N, S, p = temp[:3]
    t = temp[3:]
    fout.write('Case #' + str(i+1) + ': ')
    fout.write(str(numb(t, S, p)) + '\n')
fout.close()
fin.close()
