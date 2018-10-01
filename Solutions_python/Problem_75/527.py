import sys

file = open(sys.argv[1],'r')

testcase = int(file.readline())

for itest in range(1,testcase+1):
  
    joina=[]
    splita=[]
    input=""    
    line = file.readline()
    larr = line.split(' ')
    i=0

    c = int(larr[i])
    i+=1    

    
    tite=0
    while tite < c:
        joina.append(larr[i])
        i+=1
        tite+=1
    
    d = int(larr[i])
    i+=1

    
    tite=0
    while tite < d:
        splita.append(larr[i])
        i+=1
        tite+=1
    
    icount = int(larr[i])
    i+=1

    input=larr[i]

    
    res=[input[0]]
    i=1
    last=input[0]
  #  print "start"
    for i in range(1,icount):
 #       print "ite"
  #      print str(res)
        done=0
        chk = input[i]
        if last != '1':
            for join in joina:
                if((last == join[0] and chk== join[1]) or (last==join[1] and chk == join[0])):
                  
                    res.pop()
                    last=join[2]
                    chk=join[2]
                    res.append(join[2])
                    done=1
                    break

        if last != '1':
            for split in splita:
                for j in res:
                    if((j==split[0] and chk == split[1]) or (j == split[1] and chk== split[0])):
   
                        res=[]
                        last='1'
                        done=1
                        break

                if (res == []):
                    break
                
        if done == 0:
            last=input[i]
            res.append(input[i])
    
    

    print "Case #"+str(itest)+": "+str(res)
        
        
