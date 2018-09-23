def ans(num):
    int_prev=0
    index=-1
    for new_int in xrange(0,len(num)):
        if num[new_int] < int_prev:
            index=new_int-1
            break
        int_prev=num[new_int]
    if index==-1:
        return num
    else:
#        print index
        stop=-1
        for prev in xrange(index,-1,-1):
            if num[prev]!=num[index]:
                stop=prev
                break
#        print stop
        num9s=len(num)-1-(stop+1)
#        print "num 9s:"+str(num9s)
        changed=int(num[stop+1])-1
#        print "changed num"+str(changed)
        prev_string=num[0:stop+1]
#        print "prev_string"+str(prev_string)

        ans=prev_string+str(changed)
        for i in xrange(num9s):
            ans+="9"
        if int(ans[0])==0:
            ans=ans[1:]
        return ans
T = input()
N=[str(input()) for i in xrange(T)]
for i in xrange(len(N)):
    answer=ans(N[i])
    print "Case #"+str(i+1)+": "+answer


    
        
