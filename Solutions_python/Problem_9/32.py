def generate_list(k):
	l = [0] * k
	available = range(k)
	last = 0
	for i in range(k):
		p = available[(i +last)% len(available)]
		last = (i +last)% len(available)
		available.remove(p)
		l[p] = i+1
	return l

def main():
	num_cases = input()
	for case in range(1, num_cases+1):
		k = input()
		l = generate_list(k)
		indices = map(int, raw_input().split())
		indices = indices[1:]
		out  = []
		for i in indices:
			out.append(l[i-1])
		print "Case #%d: %s" % (case, " ".join([str(a) for a in out]))

if __name__=="__main__":
	main()
