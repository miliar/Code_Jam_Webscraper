import sys

def main():

	data = sys.stdin.read().split("\n")
	nbTest = int(data[0])
	data.pop(0)

	for i in xrange(0, nbTest):
		print "Case #%s: %s" % (i+1, sequence(int(data[0]), data[1].split(" ")))
		data.pop(0)
		data.pop(0)

def sequence(nb, seq):

	seq = [int(x) for x in seq]	
	seq.sort()

	binary = [bin(int(x)).split('b')[1] for x in seq]
	pile1 = []
	pile2 = []
	sum1 = 0
	sum2 = 0

	if int(sum_list(binary),2) != 0:
		return 'NO'
	else:
		for i in xrange(1, nb):
			pile1 = binary[:i]
			pile2 = binary[i:nb]
			
			if int(sum_list(pile1)) == int(sum_list(pile2)):
				# maximum found ?
				sum1 = sum_normal(pile1)
				sum2 = sum_normal(pile2)
				if sum1 > sum2:
					return sum1
				else :
					return sum2		

	return 'NO'
	
				
def sum_normal(l):
	res = 0
	for i in l:
		res += int(i, 2)
	return res


def sum_list(l):

	res = ''
	for i in l:
		res = addPatrick(res, i)
	return res

def addPatrick(a , b):
	# add to binary numbers like patrick
	res = ''
	
	if len(a) > len(b):
		res += a[:len(a)-len(b)]
		a = a[len(a)-len(b):len(a)]
	else:
		res += b[:len(b)-len(a)]
		b = b[len(b)-len(a):len(b)]
	
	for i in xrange(0, len(b)):
		res += str(int(((not int(a[i])) & int(b[i])) | ((not int(b[i])) & int(a[i]))))
	return res	

main()

