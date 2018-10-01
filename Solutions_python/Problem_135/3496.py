output = ""

trikov = int(input()) # number of tricks
for i in range(1, trikov + 1):
	r = int(input()) # first chosen row
	for j in range(1, 5):
		vnos = input()
		if j == r:
			line1 = set(map(int, vnos.split(" ")))
	
	r = int(input()) # second chosen row
	for j in range(1, 5):
		vnos = input()
		if j == r:
			line2 = set(map(int, vnos.split(" ")))
	
	sol = list(line1.intersection(line2))
	print("Case #", i, ": ", sep="", end="")
	if len(sol) == 0: print("Volunteer cheated!")
	elif len(sol) == 1: print(sol[0])
	else: print("Bad magician!")

print(output)
