import collections

def findOrderly(nn):
	for j in range(int(nn) - 1):
		nn = int(nn) - 1
		newm  = []
		for k in str(nn):
			newm.append(k)

		mnew = sorted(newm)
		if newm == mnew:
			return nn


filen = open('B-small-attempt0.in', 'r')

lines = filen.readlines()
xLines = lines[1:len(lines)]
caseNo = 0
start = 0

for nLine in xLines:
	n = nLine[0:len(nLine.rstrip())]

	caseNo += 1 
	m  = []
	for i in n:
		m.append(i)
	ma = sorted(m)

	if len(n) == 1:
		print("Case #" + str(caseNo) + ": " + str(n))

	elif m == ma:
		print("Case #" + str(caseNo) + ": " + str(n))

	elif m != ma:
		print("Case #" + str(caseNo) + ": " + str(findOrderly(n)))




		# for j in range(int(n) - 1):
		# 	nn = int(nn) - 1
		# 	newm  = []
		# 	for k in str(nn):
		# 		newm.append(k)

		# 	mnew = sorted(newm)
		# 	if newm == mnew:
		# 		print("Case #" + str(caseNo) + ": " + str(nn))


			# print("Case #" + str(caseNo) + ": " + str(nn))


	# elif s.count("-") == sl:
	# 	print("Case #" + str(caseNo) + ": 1")

	# elif int(k) == int(sl):
	# 	print("Case #" + str(caseNo) + ": IMPOSSIBLE")

	# else:
	# 	minus = s.count("-")
	# 	flips = 0
	# 	if s.find(start, ("-" * int(k))):
	# 		# d
	# 		if s.count("-") == 0:
	# 			print("Case #" + str(caseNo) + ": " + str(flips))


	# 		print(s.count("-" * int(k)))



		# print("Case #" + str(caseNo) + ": " + s + str(sl))
		# for i in s:
		# 	print(i)
		


		# else:
		# 	print("Case #" + str(caseNo) + ": 0")
		# print("Case #" + caseNo + ": " + flips)




	# print(nLines)
# line = lines[0].strip()


# t = 0
# s = ""
# k = len(s)
filen.close()