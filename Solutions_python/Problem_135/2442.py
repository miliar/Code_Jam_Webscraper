import os
import sys
import time

def readin():
    file = open('input.in', 'r')
    return file.readlines()

def writeout():
    global wfile
    wfile = open('out.out', 'w')

def main ():
    global inputs
    writeout()
    inputs = readin()
    cases = int(inputs[0])
    cases=cases
    for i in range(cases):
        x1 = int(inputs[i*10+1])
        x2 = int(inputs[i*10+6])
        answer=0
        matches=0
        line1 = inputs[i*10+x1+1].split()
        line2 = inputs[i*10+x2+6].split()
        print line1
        for k in range(4):
            for j in range(4):
                if line1[k]==line2[j]:
                    answer=line1[k]
                    matches=matches+1
        stri = "Case #"+str(i+1)+": "        
        if matches==0:
            stri=stri+"Volunteer cheated!\n"
        elif matches==1:
            stri=stri+str(answer)+"\n"
        else:
            stri=stri+"Bad magician!\n"
        wfile.write(stri)            
    wfile.close()

if __name__ == "__main__":
    main()