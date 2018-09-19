import math
f = open ("input.txt")
f1 = open ("output.txt", 'w')
lines = f.readlines()
count = int(lines[0])
##print(count)
##print(lines)
##for i in range(count) :
##    print(i);
##    print (lines[i+1])
##print ("\n")
for i in range(count) :
##    print (lines[i+1])
    st=lines[i+1]
    st=st.split()
    start=int(st[0])
    end=int(st[1])
##    print(st)
    count=0;
    for j in range(start,end+1):
        rt=math.sqrt(j);
        ck=rt
        ck=ck*10;
        ck=ck%10;
        if(ck!=0):
            continue
        else:
            temp=j
            rev=0
            while temp != 0:
                add=temp%10
                rev=rev*10+add
                temp=temp-add
                temp=temp/10
##            print(rev)
            if(rev==j):
                temp=rt
                rev=0
                while temp != 0:
                    add=temp%10
                    rev=rev*10+add
                    temp=temp-add
                    temp=temp/10
                if(rev==rt):
                    count=count+1
##                    print(j);
##                    print(rt);
            else:
                    continue
    st1 = ["Case #",str(i+1),": ",str(count),"\n"]
##    print(st1[0],st1[1],st1[2],st1[3])
    f1.writelines( st1 )
f.close()
f1.close()
