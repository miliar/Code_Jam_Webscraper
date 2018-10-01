

def GCD(x, y):
# The greatest common denominator (GCD) is the largest positive integer
# that divides into both numbers without a remainder.
# Examples: GCD(256,64)=64, GCD(12,8)=4, GCD(5,3)=1

        # Work With absolute values (positive integers)
	if x < 0 : x = -x
	if y < 0 : y = -y

	if x + y > 0 :
		g = y
		# Iterate Until x = 0
		while x > 0:
			g = x
			x = y % x
			y = g
		return g
	else:
		# Error, both parameters zero
		return 0
  
def solve(f, t, nums):
        nod = nums[1] - nums[2]
        for i in range(3, len(nums)):
                nod = GCD(nod, nums[1] - nums[i])

        if nod < 0 : nod = -nod
        
        y = 0
        if (nums[1] % nod) != 0:
                y = nod - (nums[1] % nod)
        f.write("Case #{0}: {1}\n".format(t, y))

  

fp = open('B-large.in', 'r')
fo = open('B-large.out', 'w')
tt = int(fp.readline())
for t in range(1, tt + 1):
        s = fp.readline().split(' ')
        nums = []
        for x in s:
                nums.append(int(x))
        solve(fo, t, nums)

fp.close()
fo.close()
