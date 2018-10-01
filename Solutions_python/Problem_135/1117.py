#!/usr/bin/env python
nin=input()
for inum in range(nin):
    rnum1=input()
    rows1=[]
    for i in range(4):
        rows1.append(raw_input().split())
    
    rnum2=input()
    rows2=[]
    for i in range(4):
        rows2.append(raw_input().split())
    set1=set();set2=set();
    for el in rows1[rnum1-1]:
        set1.add(el)
    for el in rows2[rnum2-1]:
        set2.add(el)
    set1=set1.intersection(set2)
    if(len(set1)==1):
        for element in set1:
            print "Case #%d: %d"%(inum+1,int(element))
    elif(set1!=set()):
        print "Case #%d: Bad magician!"%(inum+1)
    else:
        print "Case #%d: Volunteer cheated!"%(inum+1)
