#!/usr/bin/python3

def checkTidy(number):
    c = len(number)-1
    tidy = True
    while(tidy and c>0):
        if number[c]<number[c-1]:
            tidy = False
        c=c-1
    return tidy

def minus1(number):
    number = list(number)
    c = len(number)-1
    done = False
    while(not done):
        if(number[c]>'0'):
            number[c] = chr(ord(number[c])-1)
            done=True
        else:
            number[c]='9'
            c=c-1

    d = 0
    #print(number[d])
    while(number[d] == '0'):
        d=d+1
    #print(d)
    return (''.join(number))[d:]

def minusIntelligent(number):
    number = list(number)

    c = len(number) - 1
    number[c] = '9'
    number[c-1] = chr(ord(number[c-1])-1)

    c = c-1
    while c>0 and number[c]<number[c-1]:
        number[c] = '9'
        number[c-1] = chr(ord(number[c-1])-1)
        c=c-1

    d = 0
    #print(number[d])
    while(number[d] == '0'):
        d=d+1
    #print(d)
    return (''.join(number))[d:]

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    number = input()
    while(not checkTidy(number)):
        #number = minus1(number)
        number = minusIntelligent(number)
        #print(number)

    print("Case #{}: {}".format(i, number))
    # check out .format's specification for more formatting options
