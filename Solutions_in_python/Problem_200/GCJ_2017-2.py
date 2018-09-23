def isok(k):
    flag = 1
    k = int(k)
    last = int(k %10)
    while (not(k == 0)):
        last = k %10
        k = int(k /10)

        if( last   < (k %10)):
           flag = 0


        if(flag == 0):

             return (-1)

#      print(k)
    return 1


tests = int(input())
for j in range(0,tests):
   i = int(input())

   while(1 == 1):
      ans = isok(i)
      if(ans == 1):
          print('Case #'+str(j+1)+': '+str(i))
          break
      else:
          i = i-1

