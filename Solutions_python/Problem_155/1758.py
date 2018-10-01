input = open("A-large.in", "r")
output = open("result.out", "w")

T = int(input.readline())
case = 0
for line in input:
	case += 1
	(smax,s) = line.split()
	n = 0;
	r = 0;
	for i in range(int(smax) + 1):
		if n < i:
			r += i - n
			n += i - n
		n += int(s[i])
	output.write("Case #{}: {}\n".format(case, r))

input.close()
output.close()