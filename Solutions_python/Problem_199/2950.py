def convertToNumberArray(pancakes_string):
	numbers = []
	for letter in pancakes_string:
		if letter == "+":
			numbers.append(1)
		else:
			numbers.append(0)
	return numbers

def switch(pancakes, length, start):
	for i in range(start, start + length):
		if pancakes[i] == 0:
			pancakes[i] = 1
		else:
			pancakes[i] = 0
	return pancakes

def main():
	t = int(input())
	for i in range(1, t + 1):
		args = input().split(" ")

		pancakes = convertToNumberArray(args[0])
		length = int(args[1])

		switches = 0
		for j in range(0, len(pancakes) - length + 1):
			if pancakes[j] == 0:
				pancakes = switch(pancakes, length, j)
				switches += 1

		all_happy = True;
		for j in range(0, len(pancakes)):
			if(pancakes[j] == 0):
				all_happy = False

		answer = ""
		if all_happy:
			answer = switches
		else:
			answer = "IMPOSSIBLE"

		print("Case #{}: {}".format(i, answer))

if __name__ == '__main__':
	main()