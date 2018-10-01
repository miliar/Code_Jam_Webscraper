def solve():
    n = input()
    naomi = [float(x) for x in raw_input().strip().split()]
    ken = [float(x) for x in raw_input().strip().split()]
    naomi.sort(reverse=True)
    ken.sort(reverse=True)
    naomi_1 = naomi[:]
    ken_1 = ken[:]
    deceitfulScore = 0
    while naomi:
        if naomi[0] > ken[0]:
            deceitfulScore += 1
            naomi.pop(0)
            ken.pop(0)
        else:
            naomi.pop()
            ken.pop(0)
    normalScore = 0
    while naomi_1:
        if naomi_1[0] > ken_1[0]:
            normalScore += 1
            naomi_1.pop(0)
            ken_1.pop()
        else:
            naomi_1.pop(0)
            ken_1.pop(0)
    return deceitfulScore, normalScore

def main():
    n = input()
    for i in xrange(n):
        x1,x2 = solve()
        print "Case #%s: %s %s" %((i+1),x1,x2) 

if __name__=='__main__':
    main()
