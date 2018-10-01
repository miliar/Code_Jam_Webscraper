# pre-calculation part
# Let Xn be the expectation value that needed to sort array of length n
# Note that the array I mentioned above is in disjoint group(See the source for details)
#
# Then, Xn = 1 + Sigma_{i=0}^n (nCi * f(i) * Xi / n! ), n >= 3 
#       X0 = 0
#       X1 = 0
#       X2 = 2
#       where f(0) = 1
#            f(1) = 0
#            f(n) = (n-1) * (f(n-1) + f(n-2)),  n >= 2
# holds.
# By hand, you can aware that Xn = n.

import sys  
  
INPUT_FILE = "C:/Users/kenji/Desktop/test.in"  
OUTPUT_FILE = "C:/Users/kenji/Desktop/test.out"  
  
sys.stdin = open(INPUT_FILE, "r")  
sys.stdout = open(OUTPUT_FILE, "w")

n = raw_input()
n = int(n)

for i in range(n):
    m = raw_input()
    m = int(m)
    
    nums = raw_input()
    nums = nums.split(" ")
    nums = map(int, nums)
    nums = map(lambda x:x-1, nums)
    
    grp = []
    used = [0] * m
    for j in range(m):
        if nums[j] == j:
            continue
        if used[j]:
            continue
        
        cnt = 0
        k = j
        while used[k] == 0:
            used[k] = 1
            k = nums[k]
            cnt = cnt + 1
        
        grp = grp + [cnt]
    
    print "Case #%d: %.6lf" % (i+1, sum(grp))
    
sys.stderr.write("done!")
