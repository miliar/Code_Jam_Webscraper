def highestNonSurprising(total):
	return (total+2)/3

def highestSurprising(total):
	if total < 2: return total
	return (total+4)/3

def solve(s):
	input = [int(x) for x in s.split()]
	N = input[0]
	S = input[1]
	p = input[2]
	scores = input[3:]
	count = 0
	if p>10: return 0
	for score in scores:
		if highestNonSurprising(score) >= p: count += 1
		else:
			if S > 0 and highestSurprising(score) >= p:
				S -= 1
				count += 1
	return count




n = int(raw_input())

for i in range(1,n+1):
	print "Case #" + str(i) + ": " + str(solve(raw_input()))

 
