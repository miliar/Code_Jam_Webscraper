def solve (num):
    ans = 0
    while True:
        index = 0
        cont = 0
        while index < len(num)-1:
            if num[index] <= num[index+1]:
                cont += 1
            index += 1
        if cont == len(num)-1:
            ans = int(num)
            break
        else:
            num = str(int(num)-1)
    return ans      
    
t = int(input())
limit = t+1
for i in range (1,limit):
    number = input()
    ans = solve(number)
    print ("Case #" + str(i) + ":", ans)


'''
Created on 8 abr. 2017

@author: LAURA DE PAZ
'''
