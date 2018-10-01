n=int(input())
for i in range(n):
     need=0
     together=0
     temp = input().split()
     people,ovation=int(temp[0]),temp[1]
     for j in range(len(ovation)):
          if j>together:
               need+= j - together
               together += j - together
          together+=int(ovation[j])
     print('Case #{}: {}' . format(i+1,need))
          
     
