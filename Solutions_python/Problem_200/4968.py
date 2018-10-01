#-*-coding:utf8;-*-
#python3.6

#from itertools import count
#import re, random 

pr=print

directory = r"/storage/sdcard0/download/"
ifilename = r"B-small-attempt2.in"
ofilename = r"B-small-attempt2.out"

def getOutput(given):
    output = ''
    testNum = int(given[0].strip())
    for t in range(1, testNum+1):
        num = given[t].strip()
        #pr(num)
        if len(num)==1:
            output += 'Case #{}: {}\n'.format(t,num)
            continue
            
        i = 0
        for i in range(int(num),0,-1):
            j = 0
            iS = str(i)
            #pr(i)
            #input()
            while j<len(iS)-1 and int(iS[j])<=int(iS[j+1]):
                #pr(j, i)
                j += 1
            if j>=len(iS)-1:
                break
        output += 'Case #{}: {}\n'.format(t,i)
    return output

#READ INPUT FILE
def readInput():
    try:
        with open(directory + ifilename,"r") as f:
            lines = list(f.readlines())
            return lines
    except IOError:
        print('Check file, if it exists.')
        exit()

#WRITE TO OUTPUT FILE
def writeOutput(output):
    try:
        with open(directory + ofilename,"w") as f:
            f.write(output)
    except IOError:
        print('Check write permission.')
        exit()


if __name__ == "__main__":
    inp = readInput()
    
    out = getOutput(inp)
    	
    writeOutput(out)



