fr = open("input1.in", "r")
fw = open("output1.txt", "w")
t=int(fr.readline().strip())
#t=int(input())
for i in range(t):
    n=fr.readline().strip()
    #n=input()
    s=str(n)
    l=len(s)
    for j in range(1,l)[::-1]:
        if(s[j]<s[j-1]):
            #print(s)
            r=int("1"+"0"*(l-j))
            #print(r)
            s=str(int(s)-r)[:j]+"9"*(l-j)
            #print(s)
    #print(int(s),int(n))
    if(int(s)>int(n)):
        s=s[1:]
    n=int(s)
    #print("Case #"+str(i+1)+": "+str(n)+"\n")
    fw.write("Case #"+str(i+1)+": "+str(n)+"\n")
fw.close()
fr.close()
