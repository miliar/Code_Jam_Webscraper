import operator
f=open("test.txt","r")
T=f.readline()
T=int(T)

fo=open("output.txt","w")

cnt=1



while T>=cnt:
    n=f.readline().replace('\n','')#n number till we need to find
    n=int(n)
    num_lst=[]
    #print n
    real =n
    a=0
    b=9
    rem=0
    i=1
    
    flg=0
    while(n>0):
        #print "in n",n
        a=n%10
        #print a   
        n=n/10   
        if a>b:
            #print "a if ",a
            n=real-(rem+1)
            #print "n",n
            i=1
            real=n
            rem=0
            flg=1
        else:
            #print "a",a
            rem=i*a+rem
            #print "rem ",rem
            i=i*10
        if flg!=0 :
            b=9
            flg=0
        else:
            b=a

        
    fo.write("Case #"+str(cnt)+": "+str(rem)+"\n")
    # while(n>0):
    #     a=n%10   #1012%10=2
    #     if b>a:
    #         #reminder decreasing

    #     else:
    #         #reminder incrasing

    #     n=n/10   #1012/10
    #     b=a#2



    #fo.write("Case #"+str(cnt)+": "+str(flip_cnt)+"\n")
    


    cnt+=1
f.close
fo.close()