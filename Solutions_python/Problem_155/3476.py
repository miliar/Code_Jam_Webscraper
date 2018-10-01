import sys


if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

	t = int(f.readline())
    for tc in range(0,t):
		arr = f.readline().split()
		#smax = arr[0]
		vals = list(arr[1])
		idx = 0
		clapped = 0
		needed = 0
		for v in vals:
			v = int(v)
			if v > 0:
				if clapped < idx:
					needed += (idx - clapped)
					clapped += (v + needed)
				else:
					clapped += v
			idx += 1 
		print "Case #%d: %d"%(tc+1,needed)