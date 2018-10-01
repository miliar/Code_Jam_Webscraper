#! /usr/bin/python
import sys
__author__="nqiao"
__date__ ="$Sep 12, 2009 9:26:18 AM$"

def num_in_base(val, base, min_digits=1, complement=False,
                digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    """Convert number to string in specified base

       If minimum number of digits is specified, pads result to at least
       that length.
       If complement is True, prints negative numbers in complement
       format based on the specified number of digits.
       Non-standard digits can be used. This can also allow bases greater
       than 36.
    """
    if base < 2: raise ValueError("Minimum base is 2")
    if base > len(digits): raise ValueError("Not enough digits for base")
    # Deal with negative numbers
    negative = val < 0
    val = abs(val)
    if complement:
        sign = ""
        max = base**min_digits
        if (val > max) or (not negative and val == max):
            raise ValueError("Value out of range for complemented format")
        if negative:
            val = (max - val)
    else:
        sign = "-" * negative
    # Calculate digits
    val_digits = []
    while val:
        val, digit = divmod(val, base)
        val_digits.append(digits[digit])
    result = "".join(reversed(val_digits))
    leading_digits = (digits[0] * (min_digits - len(result)))
    return sign + leading_digits + result

def num2list(val):
    return([int(i) for i in list(str(val))])

def isHappyNum(val10base,base=10):
    flag=1
    val_pre=num_in_base(val10base, base)
    squreSet=set()
    while(flag):
        val_post=sum([i**2 for i in num2list(val_pre)])
        if val_post in squreSet:
            flag=0
            if val_post ==1:
                #print 'Is happy number!',val_post
                return(1)
            else:
                #print 'Isn\'t happy number!',val_post
                return(0)
        squreSet.add(val_post)
        val_pre=num_in_base(val_post, base)

def calHappyNum(val10base, base=10):
    flag=1
    while(flag):
        if isHappyNum(val10base, base)==1:
            return(val10base)
        else:
            val10base+=1

def parseInput(fn):
    lineNum=0
    caseDict={}
    caseNum=0
    case=1
    for line in open(fn).read().split('\n'):
        lineNum+=1
        if lineNum==1:
            caseNum=int(line)
        elif len(line)<1:
            continue
        else:
            caseDict[case]=[int(i) for i in line.split()]
            case+=1
    print 'Parse input finished!'
    return(caseDict)

def formatOutput(d,fn):
    keyList=d.keys()
    keyList.sort()
    f=open(fn,'w')
    for key in keyList:
        f.write('Case #'+str(key)+':'+' '+str(d[key])+'\n')
    f.close()
    print 'write output finished!'

if __name__ == "__main__":
    fn=sys.argv[1]
    #fn='test.in'
    caseResult={}
    caseDict=parseInput(fn)
    print caseDict
    for caseID,bases in caseDict.iteritems():
        happyVal=0
        flag=1
        numFrom=2
        while flag:
            bigBase=sorted(bases,reverse=True)[0]
            happyVal=calHappyNum(numFrom,bigBase)
            for i in sorted(bases,reverse=True)[1:]:
                if isHappyNum(happyVal, i)==1:
                    flag=0
                else:
                    flag=1
                    break
            numFrom+=1
        print caseID,happyVal
        caseResult[caseID]=happyVal
    print caseResult
    formatOutput(caseResult,fn+'.out')
    