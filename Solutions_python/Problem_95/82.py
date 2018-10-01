#!/usr/bin/python
# Filename: Problem A. Speaking in Tongues.py

#file = "Problem A. Speaking in Tongues"
#file = "Problem A. Speaking in Tongues small"
#file = "Problem A. Speaking in Tongues large"
file = "A-small-attempt0"

#debug = True
debug = False

inputExamp0 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
inputExamp1 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
inputExamp2 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"

outputExamp0 = "our language is impossible to understand"
outputExamp1 = "there are twenty six factorial possibilities"
outputExamp2 = "so it is okay if you want to just give up"

Srtmap = {}
SrtUnmap = {}
def bulidMap(inputStr,outputStr):
    assert len(inputStr) == len(outputStr)
    for i in range (len(inputStr)):
        if(" " != inputStr[i]):
            if inputStr[i] in Srtmap:
                assert Srtmap[inputStr[i]] == outputStr[i]
            else:
                Srtmap[inputStr[i]] = outputStr[i]
                SrtUnmap[outputStr[i]] = inputStr[i]


def solve(instr):
    ret = ""
    for i in range(len(instr)):
        if("\n" ==  instr[i]):
            continue
        if(" " != instr[i]):
            ret += Srtmap[instr[i]]
        else:
            ret += " "
        if debug:
            print(ret)
    return (ret)

def main():
    inFile = open(file+".in")
    assert inFile
    outFile = open(file+".out",'w')
    assert outFile
    
    T = int(inFile.readline())
    for n in range(T):
        soln = solve(inFile.readline())
        if debug:
            print ("Case #%d: %s\n" % (n+1, soln))
        outFile.write("Case #{0}: {1}\n".format(n+1, soln));
        
    inFile.close()
    outFile.close()

bulidMap(inputExamp0,outputExamp0)
bulidMap(inputExamp1,outputExamp1)
bulidMap(inputExamp2,outputExamp2)

Srtmap['z'] = 'q'
Srtmap['q'] = 'z'

if debug:
    print(Srtmap)
    print(len(Srtmap))


if debug:
    for i in range(97, 123):
        if chr(i) in Srtmap:
            print(chr(i),":",Srtmap[chr(i)])
        
main()


