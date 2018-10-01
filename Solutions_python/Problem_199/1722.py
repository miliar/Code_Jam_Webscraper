work_amount = int(input())

for t in range(work_amount):
	flipAmount = 0
	pancakes, consFlip = input().split()
	pancakes = list(pancakes)
	consFlip = int(consFlip)
	for i in range(len(pancakes)-consFlip+1):
		if pancakes[i] == "-":
			for j in range(i, i+consFlip):
				if pancakes[j] == "-":
					pancakes[j] = "+"
				elif pancakes[j] == "+":
					pancakes[j] = "-"
			flipAmount += 1
	if "-" in pancakes:
		flipAmount = "IMPOSSIBLE"
	print("Case #{}: {}".format(t+1, flipAmount))
