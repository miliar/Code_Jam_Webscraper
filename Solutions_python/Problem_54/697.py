def gcd(m, n):
    t = 0
    while(m % n != 0):
        t = n
        n = m % n
        m = t
    return n

def gcdn(a):
    if len(a) == 1: return a[0]

    ret = 0
    for i in range(len(a) -1) :
            ret = gcd(a[i], a[i+1])
            if ret == 1 : break
    
    return ret

def main():
    f = open("txt1.in")
    count = -1
    for t in f:
        count += 1
        if count == 0: continue

        t = t.strip()
        split = t.split(' ')
        split = split[1:]

        diffs = []
        for i in range(len(split) - 1) :
            diff = abs(int(split[i]) - int(split[i+1]))
            if diff != 0:
                diffs += [diff]

        
#        print(diffs)

        factor = gcdn(diffs)
        if factor == 1 : 
            print("Case #" + str(count) + ": " + str(0))
            continue

        ss = [int(i) for i in split]
        ss.sort()
        
        ans = ss[0] % factor
        if ans != 0: ans = abs(ans - factor)

        print("Case #" + str(count) + ": " + str(ans))

    f.close()

if __name__ == "__main__":
#    print(gcd(7,5))
    main()
