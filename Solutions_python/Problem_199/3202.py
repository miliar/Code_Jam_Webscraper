



def oversizedPancakeFlipper(S, K):
	result = [float('inf')]
	L = [True if x=='+' else False for x in S]
	used = [False] * len(L)
	# if not isValid(L, K):
	# 	return "IMPOSSIBLE"

	helper(L, K, 0, 0, result, used)
	if result[0] == float('inf'):
		return "IMPOSSIBLE"
	else:
		return result[0]

def helper(L, K, index, path, result, used):
	# print "L = {}".format(L)
	# print "used = {}".format(used)
	if all(L):
		result[0] = min(result[0], path)
		return

	# if all(x == False for x in L):
	# 	result[0] = min(result[0], path+1)
	# 	return


	if all(used):
		return

	for i in range(len(L)):
		if all(L[i:i+K]):
			continue

		if used[i] == False:

			used[i] = True


			if i <= len(L)-K:

				for j in range(i, i+K):
					L[j] = not L[j]

				helper(L, K, i, path+1, result, used)

				for j in range(i, i+K):
					L[j] = not L[j]

			else:

				for j in range(len(L)-K, len(L)):
					L[j] = not L[j]

				helper(L, K, i, path+1, result, used)

				for j in range(len(L)-K, len(L)):
					L[j] = not L[j]

			used[i] = False




# S = "---+-++-"
# K = 3
# print oversizedPancakeFlipper(S, K)

# S = "+++++"
# K = 4
# print oversizedPancakeFlipper(S, K)

# S = "-+-+-"
# K = 4
# print oversizedPancakeFlipper(S, K)

# S = "----"
# K = 3
# print oversizedPancakeFlipper(S, K)

# S = "-+-+"
# K = 3
# print oversizedPancakeFlipper(S, K)

# read a line with a single integer
t = int(raw_input())

for i in xrange(1, t+1):
	# read a list of integers, 2 in this case
	S, K = [s for s in raw_input().split(" ")]
	result = oversizedPancakeFlipper(S, int(K))
	print "Case #{}: {}".format(i, result)
