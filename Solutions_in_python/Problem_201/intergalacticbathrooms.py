import math

cases = int(input())
file_open = open('output3.txt', 'w')

for i in range(cases):
    inp = input().split()
    n = int(inp[0])
    k = int(inp[1])

    tier = math.floor(math.log(k, 2))

    pattern = (2**(tier+1) - 1)
    counter = 1
    while pattern < n:
        pattern += 2**tier
        counter += 1

    pattern -= 2**tier
    counter -= 1
    
    big_nums = n - pattern

    position_on_tier = k - (2**tier)

    if position_on_tier < big_nums:
        val = counter+1
    else:
        val = counter
    
    file_open.write('Case #' + str(i+1) + ': ' + str((val)//2) + ' '+ str(((val-1)//2)) + '\n')

file_open.close()
