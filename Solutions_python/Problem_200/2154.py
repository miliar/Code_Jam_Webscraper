list_=[]
def mono(number):
    if len(number)==1:
        #print('here 1')
        return 0
    for i in range(len(number)-1):
        if int(number[i])>int(number[i+1]):
            return i+1
    return 0
def sup(number):
    while mono(number):
        index=mono(number)-1
        number[index]=int(number[index])-1
        for i in range(index+1,len(number),1):
            number[i]='9'
    i=0
    while number[i]==0:
        del(number[i])
        i+=1
    return(number)
n=int(input())
for i in range(n):
    list_.append(input())
i=0
for elem in list_:
    number=[]
    for d in elem:
        number.append(d)
    result = ''
    for a in sup(number):
        result+=str(a)
    print("Case #%d: %s" % (i+1,result) )
    i+=1
    
    
