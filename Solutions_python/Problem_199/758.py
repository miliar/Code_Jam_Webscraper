def is_happy(pancake):
	if "-" in pancake:
		return False
	return True

def flip(side):
	if (side == "-"):
		return "+"
	if (side == "+"):
		return "-"

count = 0
number_of_cases = 0
file_object = open("large.input", "r")
for line in file_object:
	flips = 0
	if (count == 0):
		count += 1
		number_of_cases = int(line)
		continue
	pancake = line.replace("\n","")
	k       = int(pancake.split(' ')[1])
	pancake_list = list(pancake.split(' ')[0])
	try:
		for i in xrange(len(pancake_list)):
			if pancake_list[i] == "-":
				flips += 1
				for j in xrange(i,i + k):
					pancake_list[j] = flip(pancake_list[j])
		if (is_happy(''.join(pancake_list))):
			print("Case #{}: {}".format(count, flips))
		else:
			print("Case #{}: {}".format(count, "IMPOSSIBLE"))
		count += 1
	except:
		print("Case #{}: {}".format(count, "IMPOSSIBLE"))
		count += 1