def findls(l,i):
    j = i - 1
    while l[j] == 0:
        j -= 1
    return i-j-1

def findrs(l,i):
    j = i + 1
    while l[j] == 0:
        j += 1
    return j-i-1



def problemc(s):
    n,k = map(int,s.split())
    s = [0]*(n+2)
    s[0]  = 1
    s[-1] = 1


    j = 0
    while j<k:

        i = 0
        lsrs = list()

        for c in s:
            if c == 0:
                ls = findls(s,i)
                rs = findrs(s,i)
                lsrs.append([i,min(ls,rs),max(ls,rs)])
            i += 1

        maxmi = 0
        for m in lsrs:
            if m[1] > maxmi:
                maxmi = m[1]

        #how many maxmis?
        milsrs = list()
        for m in lsrs:
            if m[1] == maxmi:
                milsrs.append(m)

        if len(milsrs) == 1:
            o = milsrs[0][0]
            ret1 = milsrs[0][1]
            ret2 = milsrs[0][2]
        else:
            maxma = 0
            for m in milsrs:
                if m[2] > maxma:
                    maxma = m[2]

            for m in milsrs[::-1]:
                if m[2] == maxma:
                     o = m[0]
                     ret1 = m[1]
                     ret2 = m[2]

        #occupy  it
        s[o] = 1
        j += 1

    return ret1,ret2

def main():
    for c in range(1,input()+1):
        mi,ma = problemc(raw_input())
        print "Case #%d:"%c,ma,mi

if __name__ == '__main__':
    main()
