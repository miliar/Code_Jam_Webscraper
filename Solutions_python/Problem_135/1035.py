f = open('A-small-attempt2.in', 'r')

read = f.readline()
x = 0
r1 = []
r2 = []
r1_temp = []
r2_temp = []


while x<int(read):
   firstAns = f.readline()

   y = 1
   #take the row where the card is
   while y<=4:
      if y == int(firstAns):
        r1_temp = f.readline()
      else:
      	f.readline()
      y = y+1
  

   y = 1
   secondAns = f.readline()
   #take the row where the card is in the new arrangement
   while y<=4:
   	  if y==int(secondAns):
   	  	r2_temp = f.readline()
   	  else:
   	  	f.readline()
   	  y = y+1

   #tokenize
   r1 = r1_temp.split()
   r2 = r2_temp.split()

   #compare the two rows
   count = 0

   for i in r1:
   	  if i in r2 and i != '\n' and i!=' ':
   	  	card = i
   	  	count = count+1
   	  	 

   if count == 0:
   	 print 'Case #{num}: Volunteer cheated!'.format(num=x+1)
   elif count > 1:
     print 'Case #{num}: Bad magician!'.format(num=x+1)
   else:
   	 print 'Case #{num}: {card}'.format(num=x+1,card=card)

   x = x+1
f.close()