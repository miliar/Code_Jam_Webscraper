def wait(c,f,F,x):
    if( (x/f) > (c/f)+ x/(f+F)):
       return 1
    else:
       return 0

a = open('B-large.in','r')
cases=int(a.readline()[:-1])

for i in range (0,cases):
       line = (a.readline()[:-1]).split(" ")
       lineOne = []

       for j in line:
           lineOne.append(float(j))

       c = lineOne[0]
       F = lineOne[1]
       x = lineOne[2]
       time = 0
       f = 2.0

       if(x<c):
          print("Case #"+str(i+1)+": "+str(x/2))
       else:
           count = 0
           while(count<x):
               if(wait(c,f,F,x)):
                   time = time + (c/f)
                   f = f+F
               else:
                   time = time + (x/f)
                   break
           print("Case #"+str(i+1)+": "+str(time))
        
        
    
    
