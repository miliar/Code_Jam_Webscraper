
inputFile = 'input.txt'
inputFile = 'C-small-attempt0.in'
outputFile = 'output.txt'

f = open(inputFile, 'rb')
inputs = f.readlines()
f.close()

total = int(inputs[0])
count = 1
        
i = 1
result = ''

def calc1(a):
    if a == 0:
        return 0
    if a == 1:
        return 3
    if a == 2:
        return 2
    return calc1(a-2)*2
def calc2(a):
    if a == 0 or a == 1:
        return 0
    if a == 2:
        return 1
    if a % 2 == 1:
        return calc2(a-2) + 2
    else:
        return calc2(a-2) + 1
def calc(a, b, intA):
    result = 0
    isEqual = False
    if a == 1:
        if intA >= 0:
            result +=1;
            isEqual = intA==0
        if intA >= 1:
            result +=1;
            isEqual = intA==1
        if intA >= 4:
            result +=1;
            isEqual = intA==4
        if intA >= 9:
            result +=1;
            isEqual = intA==9
        return (result, isEqual)
        
    if b==1:
        result = 4
    else:
        result = calc1(b)+calc1(b-1)+calc2(b)+calc2(b-1)
    cpA = ['0' for i in range(a)]
    i = int(a/2)
    j = 0
    subA = ['0','1','2']
    subB = ['0','1']
    
    if a % 2 == 1:
        while (j < i and i > 0):
            cpA[j] = '1'
            cpA[-j-1] = '1'
            for sub in subA:
                cpA[i] = sub
                if int(''.join(cpA)) * int(''.join(cpA)) <= intA:
                    isEqual = intA==int(''.join(cpA)) * int(''.join(cpA))
                    result += 1
                else:
                    
                    return (result, isEqual)
            j+=1
    if a % 2 == 0:
        while((j==0 or j < i-1) and i > 0):
            
            cpA[j] = '1'
            cpA[-j-1] = '1'
            for sub in subB:
                cpA[i] = sub
                cpA[i-1] = sub
                if i-1 == j and sub == '0':
                    continue
                if int(''.join(cpA)) * int(''.join(cpA)) <= intA:
                    isEqual = intA==int(''.join(cpA)) * int(''.join(cpA))
                    result += 1
                else:
                    return (result, isEqual)
            j+=1
    
    cpA = ['0' for i in range(a)]
    cpA[0] = '2'
    cpA[-1] = '2'
    
    if a % 2 == 1:
        cpA[int(a/2)] = '1'
        if int(''.join(cpA)) * int(''.join(cpA)) <= intA:
            isEqual = intA==int(''.join(cpA)) * int(''.join(cpA))
            return (result + 2, isEqual)
        else:
            cpA[int(a/2)] = '0'
            if int(''.join(cpA)) * int(''.join(cpA)) <= intA:
                isEqual = intA==int(''.join(cpA)) * int(''.join(cpA))
                return (result + 1, isEqual)
            else:
                return (result,isEqual)
    else:
        if int(''.join(cpA)) * int(''.join(cpA)) <= intA:
            isEqual = intA==int(''.join(cpA)) * int(''.join(cpA))
            return (result + 1, isEqual)
        else:
            return (result,isEqual)
    
    return (result,isEqual)


def test(a, b):
    lenA = (len(str(a)) + 1) / 2
    lenB = (len(str(b)) + 1) / 2 
    
##    lastLenA = len(str(a)) /2
##    lastLenB = len(str(b)) /2
    numA,equalA = calc(lenA, lenA-1, a)
    numB,equalB = calc(lenB, lenB-1, b)

    if equalA:
        return numB - numA + 1
    else:
        return numB - numA 

while i < len(inputs):
    a, b=inputs[i].replace('\r','').replace('\n','').strip().split()
    a = int(a)
    b = int(b)
    
    i+=1
    result += 'Case #%d: ' %count + str(test(a,b)) + '\r\n'
    count += 1

f=open(outputFile,'wb')
f.write(result)
f.close()
    
