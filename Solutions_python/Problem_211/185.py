import math
f = open("C-small-1-attempt1.in")
datainput = []
for l in f:
	datainput.append(l.strip())
totcase = int(datainput[0])
case = 1
while case <= totcase:
	credit = float(datainput[3 * case - 1])
	singlep = []
	for i in datainput[3 * case].split(' '):
		singlep.append(float(i))
	singlep.sort()
	singlep = singlep + [1.0]
	tobefilled = 0
	prevlow = 0
	for i in range(len(singlep)):
		prevfilled = tobefilled
		if i == 0:
			prevlow = singlep[i]
			continue
		tobefilled += (singlep[i] - prevlow) * i
		# print("prevlow: " + str(prevlow))
		# print("singlep: " + str(singlep[i]))
		# print("tobefilled: " + str(tobefilled))
		if tobefilled >= credit:
			break
		prevlow = singlep[i]
	if tobefilled < credit:
		ji = 1
	else:
		for j in range(i):
			singlep[j] = (credit - prevfilled) / i + prevlow
		ji = 1
		for j in singlep:
			ji *= j
	print("Case #{}: {:.9f}".format(case, ji))
	case += 1