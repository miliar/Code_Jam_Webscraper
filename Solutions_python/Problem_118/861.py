import argparse

def palindromes(lo,hi):
	halfD = int(.5+len(str(hi))/2.)
	

	for h in range(10**halfD):
		si = str(h)

		#odd
		num = long(''.join([si,si[-2::-1]]))
		if num >= lo and num <= hi:
			yield num

			


		#even
		num = long(''.join([si,si[-1::-1]]))
		if num >= lo and num <= hi:
			yield num
			

def is_palindrome(num):
	numS = str(num)

	return numS==numS[-1::-1]





if __name__=='__main__':
	
	
	p = argparse.ArgumentParser(description='adsf')
	p.add_argument('infilename', nargs=1, help='ncs file to be converted')
	p.add_argument('outfilename', nargs=1, help='ncs file to be converted')

	args = p.parse_args()


	inf = open(args.infilename[0])
	outf = open(args.outfilename[0],'w')


	num = inf.readline()


	for i in range(int(num)):

		(lo,hi) = [long(a) for a in inf.readline().split()]


		roots = [a for a in palindromes(1,long(hi**.5))]
	
		outs = []
		for r in roots:
			test = r**2
			if is_palindrome(test) and test>=lo and test<=hi:
				outs.append(test)
	
	
		
		outf.write('Case #%d: %d\n'%((i+1),len(outs)))
	

