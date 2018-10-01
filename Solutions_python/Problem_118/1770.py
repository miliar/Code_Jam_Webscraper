import math 

def perfect_squares(min, max):
	lowest = int(math.ceil(math.sqrt(min)))
	heighest = int(math.sqrt(max))
	a = [n**2 for n in range(lowest, heighest + 1)]
	return a

def is_palindrome(s):
	return all(s[i] == s[-(i + 1)] for i in range(len(s)//2))

def number_palindrome(n):
	return is_palindrome(str(n))

a = perfect_squares(1,1000)
t = int(raw_input())
for i in range(0,t):
	count =0
	l = raw_input().split()
	start = int(l[0])
	stop = int(l[1])
	for j in range(start,stop+1):
		if j in a:
			if number_palindrome(j) and number_palindrome(int(math.sqrt(j))):
				count+=1
	print "Case #"+str(i+1)+": "+str(count)
