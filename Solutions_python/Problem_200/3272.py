#!/usr/bin/python
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

import fileinput



t = int(input())
#print("numLines = %d" % (t))
caseNum = 1
for line in fileinput.input():
    if caseNum > t:
        break;
    listN = list(line.strip())
    listNewTidy = list();
    
    digitThatBrokeIt = "-1";
    prevDigit = "0";
    broken = False

    for digit in listN:
        if int(prevDigit) > int(digit):
            digitThatBrokeIt = str(prevDigit)
            broken = True;
            break;
        prevDigit = digit
    
    if broken:
        #print("In Broken")
        nowBroke = False;
        for digit in listN:
            #print("digit= "+digit)
            if nowBroke:
                listNewTidy.append("9")
            elif digit is digitThatBrokeIt:
                listNewTidy.append(str(int(digitThatBrokeIt)-1))
                nowBroke = True
            else:
                listNewTidy.append(digit)
        
        prevTidyNumber = "".join(listNewTidy)
        prevTidyNumber = str(int(prevTidyNumber))
    else:
        prevTidyNumber = "".join(listN)


    print("Case #%d: %s" % (caseNum, prevTidyNumber))
    caseNum+=1

