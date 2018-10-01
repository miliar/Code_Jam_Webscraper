import os


def inverse (x):
	return '-' if x == '+' else '+'

with open("a.in", "r+") as f:
	lines = [x.strip() for x in f.readlines()]

answ = ""

for case in range(1, int(lines[0]) + 1):
	pancakes = list(lines[case].split(" ")[0])
	flipper = int(lines[case].split(" ")[1])

	idx = 0

	flips = 0

	while idx + flipper <= len(pancakes) :
		while idx + flipper <= len(pancakes) and pancakes[idx] == "+":
			idx+=1
		if idx + flipper <= len(pancakes):
			pancakes[idx:idx+flipper] = map(inverse, pancakes[idx:idx+flipper])	
			flips+=1

	if pancakes.count('-') > 0:
		answ += "Case #{0}: IMPOSSIBLE\n".format(case)
	else :
		answ += "Case #{0}: {1}\n".format(case, flips)	

with open("a.out", "w") as f:
	f.write(answ)
