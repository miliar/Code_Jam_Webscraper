#!/usr/bin/python
def output(resposta,num_test):
       print "Case #%d:"% num_test,resposta

def calc(v1,v2):
	sum = 0
	for i in range(len(v1)):
		num1 = v1[i]
		num2 = v2[i]
		sum = sum + (num1*num2)
	return sum

def analise (v1,v2):
	#print v1
	v1.sort(reverse=True)
	#print v1
	v2.sort()
	resp = calc(v1,v2)
	return resp
def main ():
       num_test = input()
       v1 = []
       v2 = []
       for case in xrange(num_test):
		n_tam = input()
	#	for i in range(2):
		num = raw_input("")
	#	print num
		v1 = map(int,num.split(" "))
		num2 = raw_input("")
	#	print num2
		v2 = map(int,num2.split(" "))
		resposta = analise(v1,v2)
	#	print v1
	#	print v2
		output(resposta,case+1)
		del v1
		del v2
		v1 = []
		v2 = []

main()

