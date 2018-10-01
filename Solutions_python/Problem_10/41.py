def main():
	import sys
	for i in range(1, int(sys.stdin.readline())+1):
		meta = map(lambda a:int(a), sys.stdin.readline().split())
		freq = map(lambda a:int(a), sys.stdin.readline().split())
		p = meta[0]
		k = meta[1]
		l = meta[2]

		if p * k < l:
			print "Case #" + str(i) + ": Impossible"
			continue

		freq.sort(lambda a, b:a>b and -1 or (a<b and 1 or 0))

		res = 0
		for j, f in enumerate(freq):
			res += f * (int(j/k) + 1)

		print "Case #" + str(i) + ": "+ str(res)

if __name__ == "__main__" : main()
