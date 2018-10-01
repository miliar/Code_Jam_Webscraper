def omino(X,r,c):
	# if (((r * c ) / x).is_integer() == False):
	# 	return 0

	if (r == 1 and c == 1):
		if (X == 1):
			return 1
		elif (X == 2):
			return 0
		elif (X == 3):
			return 0
		elif (X == 4):
			return 0

	elif (r == 1 and c == 2):
		if (X == 1):
			return 1
		elif (X == 2):
			return 1
		elif (X == 3):
			return 0
		elif (X == 4):
			return 0

	elif (r == 1 and c == 3):
		if (X == 1):
			return 1
		elif (X == 2):
			return 0
		elif (X == 3):
			return 0
		elif (X == 4):
			return 0

	elif (r == 1 and c == 4):
		if (X == 1):
			return 1
		elif (X == 2):
			return 1
		elif (X == 3):
			return 0
		elif (X == 4):
			return 0

	elif (r == 2 and c == 1):
		if (X == 1):
			return 1
		elif (X == 2):
			return 1
		elif (X == 3):
			return 0
		elif (X == 4):
			return 0

	elif (r == 2 and c == 2):
		if (X == 1):
			return 1
		elif (X == 2):
			return 1
		elif (X == 3):
			return 0
		elif (X == 4):
			return 0

	elif (r == 2 and c == 3):
		if (X == 1):
			return 1
		elif (X == 2):
			return 1
		elif (X == 3):
			return 1
		elif (X == 4):
			return 0

	elif (r == 2 and c == 4):
		if (X == 1):
			return 1
		elif (X == 2):
			return 1
		elif (X == 3):
			return 0
		elif (X == 4):
			return 0

	elif (r == 3 and c == 1):
		if (X == 1):
			return 1
		elif (X == 2):
			return 0
		elif (X == 3):
			return 0
		elif (X == 4):
			return 0

	elif (r == 3 and c == 2):
		if (X == 1):
			return 1
		elif (X == 2):
			return 1
		elif (X == 3):
			return 1
		elif (X == 4):
			return 0

	elif (r == 3 and c == 3):
		if (X == 1):
			return 1
		elif (X == 2):
			return 0
		elif (X == 3):
			return 1
		elif (X == 4):
			return 0

	elif (r == 3 and c == 4):
		if (X == 1):
			return 1
		elif (X == 2):
			return 1
		elif (X == 3):
			return 1
		elif (X == 4):
			return 1

	elif (r == 4 and c == 1):
		if (X == 1):
			return 1
		elif (X == 2):
			return 1
		elif (X == 3):
			return 0
		elif (X == 4):
			return 0

	elif (r == 4 and c == 2):
		if (X == 1):
			return 1
		elif (X == 2):
			return 1
		elif (X == 3):
			return 0
		elif (X == 4):
			return 0

	elif (r == 4 and c == 3):
		if (X == 1):
			return 1
		elif (X == 2):
			return 1
		elif (X == 3):
			return 1
		elif (X == 4):
			return 1

	elif (r == 4 and c == 4):
		if (X == 1):
			return 1
		elif (X == 2):
			return 1
		elif (X == 3):
			return 0
		elif (X == 4):
			return 1

def main():
	T = int(raw_input())

	for test in range(T):
		[X,R,C] = map(int, raw_input().split())
	
		if (omino(X,R,C) == 1):
			print ("Case #" + str(test+1) + ": GABRIEL")
		else:
			print ("Case #" + str(test+1) + ": RICHARD")

main()

