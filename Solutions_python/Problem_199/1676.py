def rev_pan(pancake):
	pancake = list(pancake)
	for i in range(len(pancake)):
		if pancake[i] == '-':
			pancake[i] = '+'
		else:
			pancake[i] = '-'
	return ''.join(pancake)

def solve(pancake, k):
	clear = '+'*100
	count = 0
	for i in range(len(pancake)-k+1):
		#print(i)
		if pancake[0] == '-':
			count += 1
			pancake = rev_pan(pancake[:k])[1:] + pancake[k:]
		else:
			pancake = pancake[1:]
		if pancake == clear[:len(pancake)]:
			break
	if pancake == clear[:len(pancake)]:
		return count
	else:
		return 'IMPOSSIBLE'
		
if __name__ == '__main__':
	tc = int(input())
	for tcidx in range(1, tc+1):
		pancake, k = input().strip().split()
		print("Case #{0}: {1}".format(tcidx, solve(pancake, int(k))))

"""
3
---+-++- 3
+++++ 4
-+-+- 4
"""