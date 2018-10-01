# Written by Juliana Zhu
# For Google Code Jam 2017
# Problem B - Simple Case
# 8 April 2017 Sydney time

def solve(boundary):
	for j in range(boundary, 0, -1):
		potential_tidy = [int(k) for k in str(j)]
		if len(potential_tidy) == 1:
			return potential_tidy

		for l in range(0, len(potential_tidy)):
			if potential_tidy[l] <= potential_tidy[l+1]:
				if l + 1 == len(potential_tidy) - 1:
					tidy_number = ''.join(str(e) for e in potential_tidy)
					return potential_tidy
			else:
				break
	return False

f = open("B-small-attempt0.in")
line = f.readline()
problems = [None] * int(line)
i = 0
while line:
	line = f.readline()
	if not line:
		break
	problems[i] = int(line.strip())
	i += 1
f.close()

for i in range(0, len(problems)):
	boundary = problems[i]
	tidy_number = solve(boundary)
	tidy_number = ''.join(str(e) for e in tidy_number)
	print("Case #{}: {}".format(i + 1, tidy_number))