def checkP(A, B):
    count = 0
    for x in xrange(A, B+1):
	t = str(x)
	for i in xrange(len(t)-1):
	    t = t[-1] + t[:-1]
	    if t[0] == '0':
		continue
	    if t == str(x):
		break
	    y = int(t)
	    if y >= A and y <= B and x < y:
		count += 1
    return count

f = open('sample', 'r')
fout = open('output', 'w')

n = int(f.readline())

for i in xrange(n):
    nums = f.readline().split(' ')
    A = int(nums[0])
    B = int(nums[1])
    output = 'Case #' + str(i+1) + ': ' + str(checkP(A, B)) + "\n"
    fout.write(output)
    
f.close()
