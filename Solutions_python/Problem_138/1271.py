#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ammar
#
# Created:     12/04/2014
# Copyright:   (c) Ammar 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    with open("inp.txt") as f:
        buff=f.readlines()
    cases=int(buff[0])
    fil=open("Out.txt","w")
    temp=0.0000001
    inc=0.0000001
    for i in range(1,cases+1,1):
        st=i*3-3+1
        N=int(buff[st])
        line=buff[st+1]
        r=line.split()
        Ns=[]
        Ks=[]
        Ns_T=[]
        for rr in r:
            Ns.append(float(rr))
            Ns_T.append(float(rr))
        line=buff[st+2]
        r=line.split()
        for rr in r:
            Ks.append(float(rr))
        Ns=sorted(Ns)
        Ks=sorted(Ks)
        Ns_T=sorted(Ns_T)
        count_Ns=0
        count_Ks=0

        for j in range(0,N,1):
            boolean=0
            for k in range(0,N,1):
                if Ns[k] > Ks[j]:
                    boolean=1
                    Ns[k]=-1
                    break
            if boolean==1:
                count_Ns+=1
            else:
                count_Ks+=1

        count_Ns_T=0
        count_Ks_T=0

        for j in range(0,N,1):
            boolean=0
            for k in range(0,N,1):
                if Ks[k] > Ns_T[j]:
                    boolean=1
                    Ks[k]=-1
                    break
            if boolean==1:
                count_Ks_T+=1
            else:
                count_Ns_T+=1

##        print str(count_Ns)+" "+str(count_Ns_T)
##        print Ns
##        print Ks
        msg="Case #"+str(i)+": "+str(count_Ns)+" "+str(count_Ns_T)
        fil.write(msg+"\n");

if __name__ == '__main__':
    main()
