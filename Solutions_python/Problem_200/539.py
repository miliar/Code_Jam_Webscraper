import math

def is_tidy(w):
	pow = 1
	temp = w
	while temp/int(math.pow(10,pow)) > 0:
		pow += 1
	pow -= 1
	end = True
	i = 0
	while pow > 0 and end:
		msb = temp/int(math.pow(10,pow))
		temp = temp - msb*int(math.pow(10,pow))
		next_msb = temp/int(math.pow(10,pow-1))
		if msb > next_msb:
			end = False
		pow -= 1
	# print 'test',w,end
	return end

def make_tidy(w):
	# print 'i',w
	pow = 1
	temp = int(w)
	while temp/int(math.pow(10,pow)) > 0:
		pow += 1
	pow -= 1
	end = True
	i = 0
	temp = w
	res = int(w)
	while pow > 0 and end:
		msb = w[len(w)-pow-1]
		# msb = temp/int(math.pow(10,pow))
		# temp = temp - msb*int(math.pow(10,pow))
		next_msb = w[len(w)-pow-1 + 1]
		# next_msb = temp/int(math.pow(10,pow-1))
		if msb > next_msb:
			# if pow - 1 > 0:
			subber = (int(next_msb)+1) * int(math.pow(10,pow-1))
			# print pow,subber
			res = int(w) - subber
			w1 = str(res)
			# pow = pow -2
			# if int(w)/int(w1) > 0:
				# print 'done'
				# pow -= 1
			i = len(w1)-pow-1+2
			while i < len(w1):
				# print w1
				w1 = w1[:i] + '9' + w1[i+1:]
				# print w1
				i += 1
			res = int(w1)
			if not is_tidy(res):
				res = make_tidy(str(res))
			end = False
		pow -= 1
	# print 'o',res
	return res

ina = raw_input()
for l in range(0,int(ina)):
	inb = raw_input()
	w = str(inb)
	res = make_tidy(w)
	
	if w == '0':
		res = 0
	case = l + 1
	name = 'Case #' + str(case) + ':'
	print name,str(res)
