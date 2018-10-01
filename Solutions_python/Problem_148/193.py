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
            count=0
            line=inputFile.readline().rstrip('\n').split(' ')
            n=int(line[0])
            x=int(line[1])
            line=inputFile.readline().rstrip('\n').split(' ')
            s=[int(temp) for temp in line]
            s.sort()
            while(len(s)!=0):
                one=s.pop()
                tempList=[temp for temp in s if one+temp<=x]
                if (len(tempList)!=0):
                        del s[s.index(tempList[-1])]
                count+=1

            res=str(count)
            with open(outname,"a") as out:
                out.write("Case #"+str(i+1)+": "+res+"\n")
        

if __name__=="__main__":
    main(sys.argv)
