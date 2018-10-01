def conv_to_bin(a_string):
	out_string = ""
	for symbol in a_string:
		if symbol == "-":
			out_string += "0"
		else:
			out_string += "1"
	return out_string


def flip(a_string, k, index):
	# a_string is in the form of a binary string eg. 1001011
	return a_string[:index] + bin(int(a_string[index:index + k], 2) ^ int("1" * k, 2))[2:].zfill(k) + a_string[index + k:]


with open("A-large.in") as f:
	with open("output.txt", "w") as g:
		t = int(f.readline().strip())
		for i in range(1, t + 1):
			[s, k] = f.readline().split()
			k = int(k)
			s = conv_to_bin(s)
			count = 0
			for j in range(len(s) - k + 1):
				if s[j] == "0":
					s = flip(s, k, j)
					count += 1
				if "0" not in s:
					break
			if "0" in s:
				g.write("Case #{}: IMPOSSIBLE\n".format(i))
			else:
				g.write("Case #{}: {}\n".format(i, count))