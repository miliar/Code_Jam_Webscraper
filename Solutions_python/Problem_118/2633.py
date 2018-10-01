
def getResult(inFile):
    T = int(inFile.readline().replace('\n',''))
    print T    
    outFile = file("C-small.out", "w")
    lookup_list = []
    createLookup(lookup_list)    
    for test_no in xrange(T):
        v1 = inFile.readline().replace('\n','').split(' ')
        A = int(v1[0])
        B = int(v1[1])
        start = A
        result = 0
        while start <= B:
            if start in lookup_list:
                result = result + 1
            start = start + 1
            
        outFile.write("Case #" + str(test_no+1) + ": " + str(result) + "\n");
        
    outFile.close()
    inFile.close()
    
def createLookup(lookup_list):
    for i in xrange(33):
        squareI = i*i;
        if isPalindrom(i) and isPalindrom(squareI):
            lookup_list.append(squareI);
        else:
            lookup_list.append(0);

def isPalindrom(n):
    num = n;
    rev = 0;
    digit = 0;
    while (num!=0):
        digit = num%10;
        rev = (rev*10) + digit;
        num = num/10;
    if(n==rev):
        return True;
    return False;
    
if __name__ == "__main__":
    inFile = file("C-small-attempt0.in")
    getResult(inFile)
