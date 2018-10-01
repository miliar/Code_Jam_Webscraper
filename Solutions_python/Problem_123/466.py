import io
import math
import sys


def put(key, value, dic):
	if key in dic:
		old_val = dic[key]
		if value < old_val:
			dic[key] = value
	else:
		dic[key] = value


def clean(dic):
	inv = dict()
	for (key, value) in dic.items():
		put(value, -key, inv)
	dic = dict()
	for (key, value) in inv.items():
		dic[-value] = key
	return dic

def f1(cur, size, ops):
	while size <= cur:
		size += size - 1
		ops += 1
	size += cur
	return size, ops
	
	
def func(A, sizes):
	states = dict()
	states[A] = 0
	
	sizes = sorted(sizes)
	#print(A, sizes)
	for cur in sizes:
		states = clean(states)
		#print(states)
		new_states = dict()
		for (key, value) in states.items():
			put(key, value + 1, new_states)
			if key > cur:
				put(key + cur, value, new_states)
			else:
				if key == 1:
					continue
				operations = math.ceil((cur + 1 - key) / (key - 1))
				if operations == 0:
					print('asdddddddddd')
					exit(1)
				new_size, new_ops = f1(cur, key, value)
				#new_size = (key + (key - 1) * operations) + cur
				#new_ops = value + operations
				put(new_size, new_ops, new_states)
		states = new_states
		new_states = dict()
	#print(states)

	res = len(sizes)
	for (key, value) in states.items():
		res = min(res, value)
	return res


def main():
	inf = open('in.txt', 'r', encoding='utf-8')
	#inf = sys.stdin
	outf = open('out.txt', 'w', encoding='utf-8')
	#outf = sys.stdout

	first_line = inf.readline()
	#print(first_line)
	T = int(first_line.rstrip())
	for test in range(T):
		A, N = inf.readline().rstrip().split()
		A = int(A)
		N = int(N)
		sizes = [int(x) for x in inf.readline().strip().split()]
				
		res = func(A, sizes)
		print('Case #' + str(test + 1) + ': ', end='', file=outf)
		print(res, file=outf)

if __name__ == '__main__':
	main()