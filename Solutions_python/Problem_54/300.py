def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

tests = input()
for test in range(1, tests + 1):
	line = raw_input().partition(" ")[2]
	num = []
	while line != "":
		curr = line.partition(" ")
		num.append(curr[0])
		line = curr[2]
	diff = []
	for i in range(0, len(num)):
		for j in range(0, i):
			diff.append(abs(int(num[i]) - int(num[j])))
	divisor = diff[0]
	for val in diff:
		divisor = gcd(divisor, val)
	print "Case #" + str(test) + ": " + str((divisor - int(num[0]) % divisor) % divisor)
