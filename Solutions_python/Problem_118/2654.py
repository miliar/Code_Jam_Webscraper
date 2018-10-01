import math


def doFairAndSquare(start,end):
    count=0;
    for j in range(start,end+1):
        if(isPalindrome(j)==1):
            root=math.sqrt(j);
            lis=str(root);
            lis=lis.split(".");
            if(int(lis[1])==0 and isPalindrome(int(lis[0]))==1):
                count=count+1;
    return count;


def isPalindrome(num):
    n=num;
    rev=0;
    while(num>0):
        dig=num%10;
        rev=rev*10+dig;
        num=num/10;
    if n==rev:
        return 1;
    else:
        return 0;



finput=open("C:\Users\Flirt\Desktop\lolo.txt","r+");
foutput=open("C:\Users\Flirt\Desktop\out.txt","w+");
number_of_cases=finput.next();
for i in range(0,int(number_of_cases)):
    count=0;
    st=finput.next();
    st=st.split();
    start= int(st[0]);
    end= int(st[1]);
    count=doFairAndSquare(start,end);
    foutput.write("Case #"+str(i+1)+": "+str(count)+"\n");
finput.close();
foutput.close();
    
    




