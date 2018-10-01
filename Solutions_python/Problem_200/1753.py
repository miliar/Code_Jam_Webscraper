  # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

import sys

def runtest(line):
	temp = '0'
	idx = 0
	ans = ''
	for ii,x in enumerate(line):
		if x > temp:
			idx, temp = ii,x
			ans+=x
		elif x < temp:
			ans = ans[:idx]+str(int(ans[idx])-1)+'9'*(len(line)-idx-1)
			return ans[1:] if ans[0]=='0' else ans
		else:
			ans+=x
	return ans

f_dir = sys.argv[1]
fo_dir = sys.argv[2]

f = open(f_dir,'r')
fo = open(fo_dir,'w')

t = int(f.readline())  # read a line with a single integer
for i in range(1, t + 1):
  # n, m = [int(s) for s in f.readline().split(" ")]  # read a list of integers, 2 in this case
  # print("Case #{}: {} {}".format(i, n + m, n * m))
  # check out .format's specification for more formatting options
  ans = runtest(f.readline()[:-1])
  fo.write("Case #"+str(i)+': '+''.join(ans)+'\n')

f.close()
fo.close()