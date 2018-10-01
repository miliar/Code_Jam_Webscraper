t = int(raw_input())
for i in xrange(1, t + 1):
    n = str(raw_input())
    for z in range(18):
        lst = []
        for j in n:
            lst.append(j)
        for l in range(len(lst) - 1):
            if int(lst[l]) > int(lst[l+1]) and int(lst[l+1])!= 0:
                for k in range(len(lst) - l - 1):
                    lst[l + k +1] = '9'
                lst[l] = str(int(lst[l])-1)
                break
            if int(lst[l]) > int(lst[l+1]) and int(lst[l+1])== 0:
                lst[l] = str(int(lst[l]) - 1)
                for k in range(l,len(lst) -1):
                    lst[k+1] = '9'
                
            l -= 1
        n = ''.join(lst)
        
    print "Case #{}: {}".format(i,int(n))
