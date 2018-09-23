def seq_check(num):
    digits = []
    while num>0:
        last = num%10
        digits.insert(0,last)
        num //= 10
    if digits == list(sorted(digits))[:]:
        return True

f = open("B-small-attempt2.in",'r')
n = f.readline()
n = int(n)
file = open('out.txt','w')
nums = f.readlines()
nums = list(map(int,nums))
#n = int(input())
for test_num in range(n):
    num_counted = nums[test_num]
    for i in range(num_counted,0,-1):
        if seq_check(i):
            #print (i)
            file.write('Case #'+str(test_num+1)+': '+str(i)+'\n')
            break;
f.close()
file.close()
   
