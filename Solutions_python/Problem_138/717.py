#!/usr/bin/env pythom
#coding: utf-8

def war(naomi, ken):
	tmp_naomi = [(x, 1) for x in naomi]
	tmp_ken = [(x,2) for x in ken]
	total = sorted(tmp_naomi+tmp_ken, key=lambda x:x[0], reverse=True)
	total = [x[1] for x in total]
	while True:
		found = False
		for i in xrange(len(total)-1):
			if total[i]==2 and total[i+1]==1:
				total = total[:i]+total[i+2:]
				found = True
				break
		if not found:
			break
	return len(total)/2

def deceive(naomi, ken):
	tmp_naomi = [(x, 1) for x in naomi]
	tmp_ken = [(x,2) for x in ken]
	total = sorted(tmp_naomi+tmp_ken, key=lambda x:x[0], reverse=True)
	# print total
	total = [x[1] for x in total]
	# print total
	# return process(total)
	point = 0
	while True:
		if not total:
			break
		elif total[-1] == 1:
			for i in xrange(len(total)):
				if total[i] == 2:
					total = total[:i]+total[i+1:-1]
					break
		else:
			for i in xrange(len(total)-2, -1, -1):
				if total[i] == 1:
					total = total[:i]+total[i+1:-1]
					point += 1
					break
	return point


def process(queue):
	if not queue:
		return 0
	elif queue[-1] == 1:
		for i in xrange(len(queue)):
			if queue[i] == 2:
				new_queue = queue[:i]+queue[i+1:-1]
				return process(new_queue)
	else:
		for i in xrange(len(queue)-2, -1, -1):
			if queue[i] == 1:
				new_queue = queue[:i]+queue[i+1:-1]
				return 1+process(new_queue)

if __name__ == '__main__':
	fname = 'D-large'
	with open('%s.in' % fname) as f, open('%s.out' % fname, 'w') as f2:
		n = int(f.readline())
		for i in xrange(n):
			num = int(f.readline())
			naomi = [float(x) for x in f.readline().strip().split(' ')]
			ken = [float(x) for x in f.readline().strip().split(' ')]
			p1, p2 = deceive(naomi, ken), war(naomi, ken)
			# print deceive(naomi, ken), war(naomi, ken)
			print p1, p2
			f2.write('Case #%s: %s %s\n' % (i+1, p1, p2))
