def tidy(lst):
    for i in range(0,len(lst)):
        if i+1<len(lst):
            if(lst[i]>lst[i+1]):
                lst[i]=lst[i]-1
                for k in range (i+1,len(lst)):
                     lst[k]=9
                tidy(lst)
        else:
            return(lst)

t = int(raw_input()) # read a line with a single integer
for j in range(1, t+1):
    n = int(raw_input())
    lst=map(int, str(n))
    a= tidy(lst)
    for i in range(0,len(a)):
        if a[i]==0:
            a.pop(i)
            break;
    num=''.join(str(s) for s in a)
    print "Case #{}: {}".format(j,num)
