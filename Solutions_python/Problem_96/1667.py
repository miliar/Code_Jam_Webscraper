#! /usr/bin/python
import sys
    
def main():
    file1=open(sys.argv[1])
    
    a=file1.readline()
    cases=int(a)
    

    

    answers=[]
    
    for x in range(cases):
        case=file1.readline()
        split=case.split()
        split.reverse()
        N=int(split.pop())
        S=int(split.pop())
        p=int(split.pop())
        numGooglers=0

        for sumNum in split:
            if int(sumNum)>=max(p,p*3-2):

                numGooglers+=1
            elif S>0 and int(sumNum)>=max(p,p*3-4):
                S=S-1
                numGooglers+=1
        
        
        answers.append(str(numGooglers))
    strings=[]
    for x in range(cases):
        string1="Case #"+str(x+1)

        string1+=": "+ answers[x]

        strings.append(string1)
    f=open("Output.txt","w")
    for x in strings:
        f.write(x+"\n")
    
def addToTranslation(dictionary,string1,string2):
    for x in xrange(len(string1)):
        dictionary[string1[x]]=string2[x]

def translate(dictionary,string):
    returnVal=""
    for x in string:
        try:
            returnVal+=dictionary[x]
        except:
            returnVal+=x
    return returnVal



if __name__ == "__main__":
    main()
