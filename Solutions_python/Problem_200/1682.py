def main():
	for TEST in range(1, int(input())+1):
		N = list(map(int, input()))

		for i in range(0, len(N)-1):
			if N[i] <= N[i+1]:
				continue

			for j in range(i+1, len(N)):
				N[j] = 9

			N[i] -= 1

			j = i
			while j > 0:
				if N[j] < N[j-1]:
					N[j-1] = N[j]
					N[j] = 9
				j -= 1

			break

		numberStr = ''.join(str(d) for d in N)
		number = int(numberStr)
		print("Case #%d: %s" % (TEST, str(number)))

main()
