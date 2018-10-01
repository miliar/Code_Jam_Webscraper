def main():
    testcases = int(raw_input())
    count = 1

    for t in range(0, testcases):
        
        n = int(raw_input())
        l = list(str(n))
        

        while len(l) != 1:
            l = list(str(n))
            if sorted(l) == l:
                break
            else:
                s = len(l)
                m = s - 1
                if m > 1:
                    for i in range(0,m):
                        if int(l[i]) > int(l[i+1]):
                            k = i + 1
                            for t in range(k,s):
                                l[t] = 0
                    
                
                liststring = ''.join(str(e) for e in l)
                n = int(liststring)
                n -= 1

        print "Case #"+str(count)+": "+str(n)
        count += 1

if __name__ == '__main__':
    main()