def finding_max_space(a):
    '''
    Finding maximum space where the next prson will occupy
    '''
    l=len(a)
    i_start=0
    i_end=l-1
    i=0
    maximum=0
    while(i<l):
        i_temp_start=i
        temp=0
        while(i<=l-1 and a[i]!="o"):
            temp+=1
            i+=1
        if(temp>maximum):
            maximum=temp
            i_start=i_temp_start
            i_end=i-1
        i+=1
    return i_start, i_end


def adding_1_person(a,start,end):
    '''
ADDING THE PERSON ON THE POSITION WHERE IT WILL BE FITS IN
    '''
    stall = end - start + 1
    t= start + stall//2
    if(stall%2==0):
        t= t - 1
    a[t]="o"


def adding_final_person(a,start,end):
    '''
    ADDING THE FINAL PERSON RETURNING THE SPACE ON THE LEFT AND THE RIGHT
    '''
    stall = end - start + 1
    if(stall%2==0):
        t=start + stall // 2 - 1
    else:
        t=start + stall//2
    ls=t-start
    rs=end-t
    return ls,rs


a=int(input())
for j in range(a):
    stall, person=list(map(int,input().split()))
    if(stall==person):
        print( "Case #%d: 0 0" % (j+1))
        continue
    elif(person==1):
        if(stall%2==0):
            rs=stall//2
            ls=stall//2 - 1
            print( "Case #%d: %d %d" % (j+1,max(ls,rs),min(ls,rs)))
        else:
            print( "Case #%d: %d %d" % (j+1,stall//2,stall//2))
        continue
    a=""
    for i in range(stall):
        a+="."
    a=list(a)
    while(person>0):
        start , end = finding_max_space(a)
        if(person-1==0):
            ls,rs=adding_final_person(a,start,end)
        else:
            adding_1_person(a,start,end)
        person-=1
    print("Case #%d: %d %d"%(j+1,max(ls,rs),min(ls,rs)))
