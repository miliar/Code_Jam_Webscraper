from sets import Set
def main():
    c = int(raw_input().strip())
    for ci in range(c):
        n = int(raw_input().strip())
        lst1 = []
        for i in range(4):
            lst1.append(map(int, raw_input().strip().split()))
        m = int(raw_input().strip())
        lst2 = []
        for i in range(4):
            lst2.append(map(int, raw_input().strip().split()))
        set1 = Set(lst1[n-1])
        set2 = Set(lst2[m-1])
        inter = set1 & set2
        if len(inter) == 0: print 'Case #%d: Volunteer cheated!' % (ci+1)
        elif len(inter) == 1: print 'Case #%d: %d' % (ci+1, list(inter)[0])
        else: print 'Case #%d: Bad magician!' % (ci+1)

if __name__ == '__main__': main()
