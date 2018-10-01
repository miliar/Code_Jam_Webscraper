def bin_check(a,b,k):
    #print "case"
    count = 0
    i=0
    
    while i <a:
        j=0
        while j<b:
            bin_a= bin(i)
            bin_b = bin(j)
            bin_and = i & j
            #ans = int(bin_and,2)
            #print bin_a,bin_b,bin_and,ans
            if bin_and < k :
                
                count+=1
                #print bin_a,bin_b,bin_and,count
            j+=1
        i+=1
    return str(count)    
                
        

file=open("c:/users/rhv/Desktop/code_jam/2014/jumble.in","r")
file1=open("c:/users/rhv/Desktop/code_jam/2014/jumble_out.txt","w")
m=file.readline()
i=0
l = m.split()


while i<int(l[0]):
    
    m1=file.readline()
    m2=m1.split()

    ans = bin_check(int(m2[0]),int(m2[1]),int(m2[2]))
    
    d = "Case #" + str(i+1) +": "+ans+"\n"
    file1.write(d)
    i=i+1

file.close()
file1.close()
