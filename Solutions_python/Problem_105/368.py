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
		"""
		try:
			d = map((lambda x: int(x)),d)
		except:
			pass
		"""
		input.append(d)

global case_num
case_num = 0

enter = 1
def problem(N,M):

	classes = []

	# need to share M with problem()
	def search(cid, c):
		if cid != c:
			if c not in classes:
				classes.append(c)
				if M[c-1][0] > 0:
					for nc in M[c-1][1:]:
						search(cid, nc)

	def search2(cid, c):
		#print "Now search with %d"%c
		if cid != c:
			if c in classes:
				#print "Dst:",c,
				return 1
			else:
				pass
				#print "%d is not in classes"%c
			if M[c-1][0] > 0:
				#print M[c-1][1:]
				for nc in M[c-1][1:]:
					if search2(cid, nc) > 0: return 1
		return 0


	# class id
	cid = 1
	for Mi in M:
		#print "cid:",cid
		num = Mi[0]
		if num > 1:
			cs  = Mi[1:]

			i = 1
			# c is class, cs is classes
			#print "cs:",cs
			for c0 in cs:
				classes = []
				search(cid, c0)
				#print "classses:",classes
				if len(cs)-1 >= i:
					for c1 in cs[i:]:
						if search2(cid, c1) > 0:
							#print "Src:",cid
							return "Yes"
				i += 1
		cid += 1

	return "No"

T = input[0]
#print T
N=0
M=[]

for i in input[1:]:
	if N==0:
		N=int(i[0])
	else:
		M.append(map((lambda x: int(x)),i))

	if len(M) >= N:
		case_num += 1
		print "Case #%s:"%case_num,"%s"%problem(N,M)
		N=0;M=[]





