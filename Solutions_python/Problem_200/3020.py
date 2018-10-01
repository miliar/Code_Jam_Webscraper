def tidy(n):
    prev = n[0]
    for x in n:
        if prev > x:
            return False
        prev = x
    return True
                
t = int(input())

for i in range(1, t + 1):
    n = input() 

    if tidy(n):
        pass
        print("Case #{0}: {1}".format(i, n))
        continue

    #check which digit is out of order
    for a in range(0, len(n) - 1):
        if n[a] >= n[a + 1]:
            break 

    
    if a == 0 and n[a] == '1':
        print("Case #{0}: {1}".format(i, '9'*(len(n)-1)))
    else:
        print("Case #{0}: {1}".format(i, n[:a] + str(int(n[a]) - 1) + len(n[a+1:])*'9'))
