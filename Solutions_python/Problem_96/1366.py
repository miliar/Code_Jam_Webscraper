import sys

this_prog = sys.argv[:1][0]
in_args  = sys.argv[1:]
in_count = len(in_args)

target_input = in_args[0]

global debug
debug = 0
if in_count > 1:
        debug =  int(in_args[1])

f = open(target_input,'r')
data = f.read()
input = []
for d in data.split("\n"):
	if d:
		d = d.split(" ")
		try:
			d = map((lambda x: int(x)),d)
		except:
			pass
		input.append(d)

global case_num
case_num = 0

def problem(n,s,p,t):
	t.sort()
	#print n,s,p,t
	sum = 0
	for ti in t:
		if ti >= p :
			tip = ti-p

			if tip % 2 == 0:
				tiph = tip/2
			else:
				# smaller one
				tiph = (tip-1)/2

			if s > 0:
				if p-2<=tiph:
					sum += 1
					s -= 1
			else:
				if p-1<=tiph:
					sum += 1
		else:
			continue

	return sum


T = input[0]
#print T
for i in input[1:]:
	case_num += 1
	# i[0]=N, i[1]=S, i[2]=p, i[3:]=[t_i]
	print "Case #%s:"%case_num,problem(i[0],i[1],i[2],i[3:])
	indata = []
