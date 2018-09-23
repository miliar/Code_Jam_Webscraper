def solve2(ohd, oad, ohk, oak, b, d):
	cstate = [[ohd, oad, ohk, oak]]
	count = 0
	while cstate:
		count += 1
		tstate = []
		for hd, ad, hk, ak in cstate:
			if hd>0:
				if hk <= 0:
					return str(count)
				else:
					if count%2 == 1:
						if hd > ak:
							tstate.append([hd, ad, hk-ad, ak])
							if b>0:
								tstate.append([hd, ad+b, hk, ak])
							tstate.append([ohd, ad, hk, ak])
						if hd+d-ak>0:
							tstate.append([hd, ad, hk, ak-d])
						print "hi"
					else:
						tstate.append([hd-ak, ad, hk, ak])
						print "bye"


		cstate = tstate
		print count, cstate
		if count > 12:
			break
	return "Impossible"
def adder(dict, hd, ad, hk, ak):
	tmp = dict
	flag = False

	if hd not in tmp:
		flag = True
		tmp[hd] = {}
	tmp = tmp[hd]

	if ad not in tmp:
		flag = True
		tmp[ad] = {}
	tmp = tmp[ad]

	if hk not in tmp:
		flag = True
		tmp[hk] = []
	tmp = tmp[hk]

	if ak not in tmp:
		flag = True
		tmp.append(ak)

	return flag




def solve(ohd, oad, ohk, oak, b, d):
	count = 1
	cstate = []
	dict = {}
	if oad > 0:
		cstate.append([ohd, oad, ohk-oad, oak])
	if b>0:
		cstate.append([ohd, oad+b, ohk, oak])
	if d>0:
		if oak-d>0:
			cstate.append([ohd, oad, ohk, oak-d])
		else:
			cstate.append([ohd, oad, ohk, 0])

	while cstate:
		tstate = []
		for hd, ad, hk, ak in cstate:
			if hk <= 0:
				return str(count)
			if hd>ak:
				# attack
				tstate.append([hd-ak, ad, hk-ad, ak])

				# buff
				if b>0:
					tstate.append([hd-ak, ad+b, hk, ak])

				# cure
				tstate.append([ohd, ad, hk, ak])

				# d
				if d>0:
					if ak-d <= 0:
						tstate.append([hd-ak, ad, hk, 0])
					else:
						tstate.append([hd-ak, ad, hk, ak-d])
		count += 1
		cstate = []
		for hd, ad, hk, ak in tstate:
			if adder(dict, hd, ad, hk, ak):
				cstate.append([hd, ad, hk, ak])
	return "Impossible"



if __name__ == "__main__":

	import time
	start_time = time.time()

	with open("output", 'w') as fout:
		f = open("C-small-attempt0.in")
		n = int(f.next())
		for i in range(n):
			hd, ad, hk, ak, b, d = map(int, f.next().split())
			fout.write("Case #"+str(i+1)+": "+solve(hd, ad, hk, ak, b, d)+"\n")
			
		f.close()