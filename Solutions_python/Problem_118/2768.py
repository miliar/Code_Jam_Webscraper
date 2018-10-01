import math

def isPalSq(number):

	if number[::-1]!=number:
		return False

	inteiro = long(number)
	raiz = math.sqrt(inteiro)
	raiz_long = long(raiz)

	if raiz_long != raiz:
		return False

	number = str(raiz_long)

	if number[::-1]!=number:
		return False

	return True

if __name__ == '__main__':
	count = 0
	casos = raw_input()
	resultado = ""

	for cs in xrange(0,long(casos)):
		command = raw_input().split(" ")
		min = long(command[0])
		max = long(command[1])
		count = 0
		for i in xrange(min,max+1):
			if(isPalSq(str(i))):
				count+=1
		resultado += "Case #"+str(cs+1)+": " + str(count)+"\n"

	print resultado
