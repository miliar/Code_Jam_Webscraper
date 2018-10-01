import sys

input_file = sys.stdin
output_file = sys.stdout

t = int(input_file.readline().strip())

for i in range(t):
	line = input_file.readline().split()
	n = int(line[0])

	hallway = []
	button = []
	time = []
	for j in range(n):
		hallway.append(line[1 + 2 * j])
		button.append(int(line[2 + 2 * j]))

		timestamp = button[j]
		if (0 < j):
			if (hallway[j] == hallway[j - 1]):
				timestamp = time[j - 1] + abs(button[j] - button[j - 1]) + 1
			else:
				timestamp = time[j - 1] + 1
				k = j - 1
				while ((0 <= k) and (hallway[j] != hallway[k])):
					k -= 1

				if (0 <= k):
					if timestamp < time[k] + abs(button[j] - button[k]) + 1:
						timestamp = time[k] + abs(button[j] - button[k]) + 1
				else:
					if timestamp < button[j]:
						timestamp = button[j]

		time.append(timestamp)

	output_file.write("Case #" + str(i + 1) + ": " + str(time[n - 1]) + "\n")

