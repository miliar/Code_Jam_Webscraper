s = [] #MaxShyness per cases
A = [] #Audience
I2 = [0,0] #stores 2nd input
inputfile = open('A-small-attempt5.in','r')
def getfriends(a,s):
    stand = 0 #stood up
    friends = 0
    difference = 0
    for x in range(0,s+1):
        if stand>=x and int(a[x])!=0:
           stand = stand+int(a[x])
        elif int(a[x])!=0:
            difference = x - stand
            friends = friends + difference
            stand = stand+friends+int(a[x])
    return friends
    

for x in range(101):
    s.append(0)
    A.append(0)
while True:
    #C=int(input()) #Case numbers
    C=int(inputfile.readline())
    if 1<=C<=100: #Limits total case number
        for x in range(0,C):
            while True:
                #i2 = input()
                i2=str(inputfile.readline())
                i2 = i2.rstrip('\n')
                I2 = i2.split(' ',1)
                s[x]=int(I2[0])
                A[x]=I2[1]
                if 0<=s[x]<=6 and len(I2[1])==s[x]+1 and int(A[x][-1:len(A[x])])!=0:
                    break
        for x in range(0,C):
            output = 'Case #'+str(x+1)+': '+str(getfriends(A[x],s[x]))
            print(output)
