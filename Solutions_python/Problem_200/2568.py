import re

def listtoint(l):
    num = 0
    for i in l:
        num*=10
        num+=int(i)
    return num

def inttolist(num):
    return re.findall('\d',str(num))

def isTidy(num):#accepts either list or num
    digits = num
    if(type(num)!=list):
        digits = re.findall('\d',str(num))
    for i in range(0,len(digits)-1):
        if int(digits[i])>int(digits[i+1]):
            #print ("untidy")
            return False
    #print "tidy"
    return True

def preTidy(num):
    if type(num)==list:
        num = listtoint(num)
    while(isTidy(num)==False):
        num -= 1
    return num

def tidyUp(digits):
    if type(digits)==int or type(digits)==long:
        digits = re.findall('\d',str(digits))

    i=1
    while i<=len(digits):
        if isTidy(digits[0:i]):
            i+=1
        else:
            #digits = inttolist(preTidy(digits[0:i]))+digits[i:len(digits)]
            #digits = inttolist(preTidy(digits[0:i]))+['9']*(len(digits)-i)
            digits = inttolist(listtoint(digits[0:i])-1)+['9']*(len(digits)-i)
            print digits
            i=1
    return listtoint(digits)



i = 0;
qfile = open("question.txt")
afile = open("answer.txt",'w+')
t = int(re.findall('\d+',qfile.readline())[0])
for i in range(1,t+1):
    line = qfile.readline()
    afile.write("Case #"+str(i)+": "+str(tidyUp(long(line))))
    afile.write("\n")
