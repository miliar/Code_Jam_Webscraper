#Codejam C Solution


from math import sqrt

def main():
	input=open("C-small-attempt0.in",'r')
	output=open("3.out","w")
	total=int(input.readline())

	for i in range(1,total+1):
		result=0
		a=input.readline().split(" ")
		x=int(a[0])
		y=int(a[1])
		# print x,y
		for num in range(x,y+1):
			sqrtnum=sqrt(num)
			intsqrtnum=int(sqrtnum)
			if sqrtnum==intsqrtnum:
				# print num,
				if fair(num)==True:
					# print num,
					# print (int(sqrt(num)))
					if fair(intsqrtnum)==True:
						# print num,
						result+=1
						# print result
		
		# print "Case #%d: %s" %(i, result)
		output.write("Case #%d: %s\n" %(i, result))

def fair(num):
	strnum=str(num)
	numLength=len(strnum)
	end=1+numLength/2
	for i in range(0, end):
		if strnum[i]!=strnum[-(i+1)] :
			return False
	return True

main()
