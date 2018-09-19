from __future__ import division
def function(current_speed,C,F,X):
    op1=(C/current_speed)+(X/(current_speed+F))
    op2=X/current_speed
    #print op1,op2
    return op2 > op1
def current_speed(F,i):
    return 2+F*i
        
def main():
    a=open("B-large (1).in","r")
    b=open("answerrrr.out","w")
    q=a.readline()
    #q=input()
    q=int(q)
    u=1
    while(q>0):
        time=0
        #C,F,X=map(float,raw_input().split())
        C,F,X=map(float,a.readline().split())
        #print C,F,X
        flag=True
        i=0
        while(flag):
            speed=current_speed(F,i)
            i=i+1
            if function(speed,C,F,X):
                time=time+(C/speed)
            else:
                flag=False
        time=time+(X/speed)
        b.write("Case #"+str(u)+": "+str(time)+'\n')
        u=u+1
        q=q-1



                           
                        
    
if __name__ == "__main__":
    main()
