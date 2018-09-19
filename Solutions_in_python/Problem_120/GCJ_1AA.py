import sys
sys.stdin=open("A-small-attempt0.in")
sys.stdout=open("outa.txt","w")
N = int(input())
def linsearch(t,r):
    x=0
    while(True):
        if t-(2*r+4*x+1)<0:
            return x
        else:
            t-=2*r+4*x+1
            x+=1
##def expsearch(t,r):
##    guess=1
##    while(True):
##        if t-(2*r*guess+guess+(guess*(guess+1))/2)<=0:
##           #print(guess)
##          # print(int(t-(2*r*guess+guess+(guess*(guess+1))/2)),int(r+2*guess))
##          return int(guess/2)
##           #return int(guess+linsearch(int(t-(2*r*guess+guess+(guess*(guess+1))/2)),int(r+2*guess)))
##        guess*=2
for _ in range(N):
    r,t=(int(x) for x in input().split())
    #print (r,t)
    print("Case #"+str(_+1)+": "+str(linsearch(t,r)))
sys.stdout.close()
