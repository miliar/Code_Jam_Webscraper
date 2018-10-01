# coding=latin-1 

if __name__ == '__main__':
    
    n = int(raw_input())
    
    for k in range(1, n+1):
        count = 0
        myline = raw_input()
        numbers = myline.split()
        a = int(numbers[0])
        b = int(numbers[1])
        if (a < b):
            lungh = len(str(a))
            ran = range(lungh)
            j = a
            while j < b :
                jstr = str(j)
                ind = 1
                listatemp = []
                for ind in ran:
                    temp = jstr[ind:]+jstr[:ind]
                    inttemp = int(temp)
                    if inttemp > j and inttemp <= b and inttemp != a and inttemp not in listatemp:
                        count += 1
                    listatemp += [inttemp]
                j += 1
            
        print "Case #"+str(k)+": "+str(count)
        
