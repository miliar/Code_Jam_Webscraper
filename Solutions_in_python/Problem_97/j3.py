
def shift(i):
	return str(i)[-1] + str(i)[0:-1]

def main():
	fn = raw_input('File name: ')
	fin = open(fn)
	o = open('output.txt','w')
	no_iter = int(fin.readline())
	for x in xrange(no_iter):
		para = fin.readline().split(' ')
		o.write("Case #"+str(x+1) + ": " + j3(int(para[0]),int(para[1])) + '\n')
	fin.close()
	o.close()


def j3(lower,upper):
	count = 0

	for i in range(lower,upper+1):
		current = str(i)
		for j in range(len(str(i))-1):
			current = shift(current)
			if int(current) <= upper and int(current) >= lower and i < int(current):
				count += 1

	return str(count)

main()
