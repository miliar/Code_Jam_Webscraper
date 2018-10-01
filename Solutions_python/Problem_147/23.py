import sys
import os.path

def main(argv):
    if (len(argv)==1):
        print("No argument!\n")
        return
    
    if(not os.path.isfile(argv[1])):
        print("input file does not exist!\n")
        return

    inname=argv[1]
    outname=argv[1][:-2]+'out'

    with open(inname,"r") as inputFile:
        num=int(inputFile.readline())
        for i in range(num):
            res=""
            line=inputFile.readline().rstrip('\n').split(' ')
            n=int(line[0])
            m=int(line[1])
            k=int(line[2])
            if(m<=2 or n<=2):
                res=str(k)
            elif(k==5):
                res='4'
            elif(k<5):
                res=str(k)
            else:
                st=2*m+2*n-8
                encl=m*n-4
                if(k>encl):
                    res=str(st+k-encl)
                else:
                    res=str(st-(encl-k)//2)


            with open(outname,"a") as out:
                out.write("Case #"+str(i+1)+": "+res+"\n")
        

if __name__=="__main__":
    main(sys.argv)
