f=open('C:/Users/compaq/Desktop/A-small-attempt0.in','r')
f2=open('C:/Users/compaq/Desktop/small_output.txt','w')
t=int(f.readline().split()[0])

for test_case in xrange(t):
    total,people=f.readline().split()
    total=int(total)
    #print total,people
    already_standing=0
    requirement=0
    for needed in xrange(total+1):
        new_people=int(people[needed])
        if needed>already_standing and new_people!=0:
             #print "requirement is ",requirement,"needed is ",needed,"already is ", already_standing
             requirement+=(needed-already_standing)
             already_standing+=((needed-already_standing)+new_people)
             
        else:
          already_standing+=new_people      
        
    out="Case #"+str(test_case+1)+': '+str(requirement) 
    f2.write(out+'\n')  
f.close()
f2.close()    
     