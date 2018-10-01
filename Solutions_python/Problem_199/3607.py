__author__ = 'Tuhin Kundu'
def flip(ch):
    if ch=="+":
        return "-"
    else:
        return "+"
with open("B-small-attempt1.in","r") as input,open("sampout.txt","w") as output:
    t=int(input.readline())
    for j in xrange(1,t+1):
        s,k=map(str,input.readline().split())
        k=int(k)
        s=list(s)
        cnt=0
        for i in xrange(len(s)-k+1):
            if s[i]=="-":
                cnt+=1
                for q in xrange(k):
                    s[i+q]=flip(s[i+q])

            #print s
        if "-" in s:
            cnt=-1

        if cnt==-1:
            output.write("Case #"+str(j)+": IMPOSSIBLE"+"\n")
        else:
            output.write("Case #"+str(j)+": "+str(cnt)+"\n")