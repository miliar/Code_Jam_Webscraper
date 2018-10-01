
def main():

	NumberOfTestCases = int(input())

	for T in range(1, NumberOfTestCases+1):

		R, C = map(int, input().split())

		cake = [list(input()) for r in range(R)]

		print( "Case #" + str(T) + ':' )
		show(cut(cake))

def cut(cake):

	cake = vertical(cake)

	cake = list(map(list, list(zip(*cake))))

	cake = vertical(cake)

	cake = list(map(list, list(zip(*cake))))
	# cake = hori(cake)

	return cake


def vertical(cake):

	for i, row in enumerate(zip(*cake)):

		current = None

		for j, c in enumerate(row):

			if c != '?':

				current = c

			elif c == '?' and current != None:

				cake[j][i] = current

			else: continue

	cake = list(reversed(cake))

	for i, row in enumerate(zip(*cake)):

		current = None

		for j, c in enumerate(row):

			if c != '?':

				current = c

			elif c == '?' and current != None:

				cake[j][i] = current

			else: continue

	cake = list(reversed(cake))

	return cake


# def hori(cake):


# 	cake = list(zip(*cake))
# 	show(cake)

# 	for i, row in enumerate(cake):

# 		current = None

# 		for j, c in enumerate(row):

# 			if c != '?' and current == None:

# 				current = c
# 				start_index = j

# 			elif c == current: continue

# 			elif c != current and current != None:

# 				if all([cake[i-1][k] == '?' for k in range(start_index, j)]):

# 					for k in range(start_index, j): cake[i-1][k] = current

# 				current = None

# 			elif c == '?' and current == None: continue

# 			else:
# 				print('woops')
# 				print(row)
# 				print(c)

# 	cake = list(zip(*cake))






# 	return cake


def show(cake): return [print("".join(row)) for row in cake]


main()
