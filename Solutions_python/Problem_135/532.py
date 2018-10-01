def read_file(filename):
    """
    reads file and makes it into a list
    """
    f = open(filename, 'r')
    lis = []
    for line in f:
        lis.append(line.strip())
    
    f.close()
    return lis


def run(lis):
    T=int(lis[0])
    del lis[0]
    
    for i in range(T):
        input1=int(lis[i*10])
        input2=int(lis[i*10+5])
        
        row1=str(lis[(i*10)+input1])
        row2=str(lis[(i*10)+5+input2])
        
        array1=row1.split()
        array2=row2.split()
        
        set1=set(array1)
        set2=set(array2)
        
        unique=set1.intersection(set2)
        
        if len(unique)==1:
            print "Case #" +str(i+1) + ": " + " ".join(str(x) for x in unique)
        elif len(unique)==0:
            print "Case #" +str(i+1) + ": Volunteer cheated!"
        else:
            print "Case #" +str(i+1) + ": Bad magician!"

run(read_file("magic.txt"))