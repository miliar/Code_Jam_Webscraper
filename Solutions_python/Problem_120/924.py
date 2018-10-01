import math
f = open('A.in', 'r')
a=f.readline()
print(a)
f1=open('output2.txt','w')

for x in range(int(a)):
    m=f.readline()
    m=m.split()
    r=int(m[0])
    #print ('char'+str(r))
    t=int(m[1])
    #print (t)
    paintRem=int(t)
    #print (paintRem)
    #firstCircle=(2*int(r))+1
    #print (firstCircle)
    counter=0
    while (paintRem>=0):
     #   print('ew')
        firstCircle=(2*int(r))+1+(4*counter)
        paintRem=paintRem-firstCircle
      #  print(paintRem)
      #  print(firstCircle)
        counter=counter+1
    print(counter-1)
    f1.write("Case #"+str(x+1)+": "+str(counter-1)+'\n')
    
f1.close()
#print('HI')
