#read input
inputfile = open('C-small-attempt0.in')
lines = inputfile.readlines()
inputfile.close()
cases = int(lines[0])
count = 1
output = ''
while(count <= cases):
   case = lines[count]
   case = case.split(' ')
   maximum = int(case[1])
   minimum = int(case[0])
   y = 0
   for number in range(minimum,maximum+1):
      length = len(str(number))
      if(length == 2):
         ab = number
         ba = int(str(number)[1]+str(number)[0])
         if(ba>ab and ba!=ab and ba<=maximum):
            y += 1
      elif(length == 3):
         abc = number
         cab = int(str(number)[2]+str(number)[0]+str(number)[1])
         bca = int(str(number)[1]+str(number)[2]+str(number)[0])
         if(cab>abc and cab!=abc and cab<=maximum):
            y += 1
         if(bca>abc and bca!=abc and bca<=maximum):
            y += 1
      elif(length == 4):
         abcd = number
         dabc = int(str(number)[3]+str(number)[0]+str(number)[1]+str(number)[2])
         cdab = int(str(number)[2]+str(number)[3]+str(number)[0]+str(number)[1])
         bcda = int(str(number)[1]+str(number)[2]+str(number)[3]+str(number)[0])
         if(dabc>abcd and dabc!=abcd and dabc<=maximum):
            y += 1
         if(cdab>abcd and cdab!=abcd and cdab<=maximum):
            y += 1
         if(bcda>abcd and bcda!=abcd and bcda<=maximum and bcda!=dabc and bcda!=cdab):
            y += 1
   print 'Case #%d: %d' % (count,y)
   output += 'Case #%d: %d\n' % (count,y)
   count += 1
outputfile = open('output','w')
outputfile.write(output)
outputfile.close()
#end prog ... 1212 and 2121
#codejam 2012 problem A ...
