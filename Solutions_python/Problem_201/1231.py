import queue


with open("C-small-1-attempt0.in") as f:
	with open("output.txt", "w") as g:
		t = int(f.readline().strip())
		for i in range(1, t + 1):
			[n, k] = map(int, f.readline().split())
			my_queue = queue.PriorityQueue()
			my_queue.put(-n)
			for _ in range(k):
				tmp = -my_queue.get() - 1
				a = tmp // 2 + tmp % 2
				b = tmp // 2
				my_queue.put(-a)
				my_queue.put(-b)
			g.write("Case #{}: {} {}\n".format(i, a, b))