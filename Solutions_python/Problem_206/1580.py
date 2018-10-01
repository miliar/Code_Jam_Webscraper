from itertools import cycle
def main():
	filename = "in"
	data = open(filename,'r').read().strip().split()
	data = [int(x) for x in data]
	data = cycle(data)
	p = 0
	t = data.next()
	while p<t :
		p += 1
		d,n = data.next(),data.next()
		max_times = 0.0
		while n>0 :
			n-=1
			k,s = float(data.next()),float(data.next())
			time = (d-k)/s
			max_times = max(max_times,time)
			# print k,split
		res = d/max_times
		print ''.join(['Case #',str(p),': ',str(res)])



if __name__ == '__main__':
	main()