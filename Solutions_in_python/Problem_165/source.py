import math;
for t in range(0,(int)(input())):

 listint = list(map(int, input().split(' ')))
 result=(math.ceil((listint[1]*listint[0])/listint[2])-1)+ listint[2]
 print("case #",t+1,": ",(int)(result),sep="")
