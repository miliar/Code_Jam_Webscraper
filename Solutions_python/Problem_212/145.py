def printer(case, s):
    
    print("Case #%d: %d" %(case+1, s))

def cho(n,p,g):
    if p == 2:
        return len([x for x in g if x==0])+ (len([x for x in g if x==1])+1)//2
    if p == 3:
        ans = len([x for x in g if x==0])
        g = [x for x in g if x!=0]
        ones = len([x for x in g if x==1])
        twos = len([x for x in g if x==2])
        if ones == twos:
            return ans+ones
        if ones > twos:
            ones,twos = twos,ones
        if ones < twos:
            twos-=ones
            return ans+ones+(twos+2)//3
    ans = len([x for x in g if x==0])
    g = [x for x in g if x!=0]
    ones = len([x for x in g if x==1])
    twos = len([x for x in g if x==2])
    threes = len([x for x in g if x==3])
    ans += twos//2
    twos %= 2
    if ones < threes:
        ones,threes = threes,ones
    ans += threes
    ones-=threes
    threes = 0
    if twos == 1:
        if ones>=2:
            ans += 1
            ones -= 2
            twos-=1
        else:
            ans+=1
            return ans
    
    ans += (ones+3)//4
    return ans



q = int(input())

for case in range(q):
    n,p = [int(x) for x in input().split()]
    g = sorted([int(x)%p for x in input().split()])
    printer(case,cho(n,p,g))
