# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    currentNum = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    #print("Case #{}: {} {}".format(i, n + m, n * m))
    # check out .format's specification for more formatting options
    
    
    
    while True:
        #check each number to see if it is weakly increasing
        digits = []
        a = currentNum[0]
        
        while a > 0:
            digits.append(int(a % 10))
            a /= 10
        digits = digits[::-1]
        
        if sorted(digits) == digits:
            print('Case #' + str(i) + ': ' + str(currentNum[0]))
            break
        currentNum[0] -= 1

    
            
            
        
        
        
        
