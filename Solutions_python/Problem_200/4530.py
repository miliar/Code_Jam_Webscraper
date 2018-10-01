import math


def len(n):
	if (n is 0): return 0
	return int(math.log10(n))+1

def at(n, i, size):
	## note forced floor division operator //
	return int((n%10**(size-i))//(10**(size-i-1))) 


for x in range(1,int(input())+1):
	
	n = int(input()) # the number
	s = len(n) # s for size
	i = 0

	while i < s-1:
		
		temp = at(n,i+1,s) # current digit


		if (at(n,i,s)>temp): # previous digit is higher
			# sets i-th digit minus one, all trailing digits 9
			## Note again forced int division // some strange results else
			n = int(n//10**(s-i-1))*10**(s-i-1)-10**(s-i-1)+10**(s-i-1)-1
			i = -1
			s = len(n)

		i += 1

	print("Case #"+str(x)+": "+str(n))

