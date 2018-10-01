




def main():

	NumberOfTestCases = int(input())

	for T in range(1, NumberOfTestCases+1):

		N = list(map(int, list(input())))

		print( "Case #" + str(T) + ": " + str(tidy(N)) )



def intify(l): return int(''.join(map(str, l)))


def tidy(N):

	if len(N) == 1: return int(N[0])

	for i in range(len(N)-1):

		if N[i] > N[i+1]:

			return intify(N[:i] + [N[i] - 1] + [9] * (len(N) - i - 1))

		if N[i] == N[i+1]:

			for n in N[i+2:]:

				if N[i] < n: break

				elif N[i] == n: continue

				else: # N[i] > n

					return intify(N[:i] + [N[i] - 1] + [9] * (len(N) - i - 1))


	return intify(N)


main()

111111111111111110
99999999999999999
111111111111111109
