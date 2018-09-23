
from itertools import groupby

def flip(a):
	if a == '+':
		return '-'
	if a == '-':
		return '+'
def flip_stack(seq, n, start_idx ):
	seq_flip = seq[start_idx : n + start_idx]
	seq_flip_done =  ''.join(map(lambda x : flip(x),  seq_flip))
	return seq[:start_idx] + seq_flip_done + seq[n+start_idx :]

def get_rest_minus(seq):
	cnt = 0
	for i in reversed(seq):
		if i == '+':
			break
		if i == '-':
			cnt += 1
	return cnt   

def check_bias_sec(seq) :
	grouped_seq = []
	for key , group in groupby(seq):
		grouped_seq.append(key)
	if grouped_seq == ['+'] or grouped_seq == ['+','-'] or grouped_seq ==['-']:
		# print  "check bias true"
		return True 
	else:
		# print  "check bias false"
		return False 

def find_first_minus(seq):
	for i, e in enumerate(seq) : 
		if e == '-':
			return i
	return None
		


if __name__ == '__main__' : 
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
	    	seq, width = raw_input().split()
		width = int(width)
		seq = seq.strip()
		impossible = False 
		step = 0
		while (True):
			if '-' not in seq:
				break; 
			if check_bias_sec(seq) and get_rest_minus(seq)< width :
				impossible = True 
				break
			else:
				first_minus = find_first_minus(seq)
				# print first_minus
				seq = flip_stack(seq, width, first_minus )
				step+=1

		if impossible : 
			print "Case #%d: IMPOSSIBLE"%(i)
		else:
	    		print "Case #%d: %d"%(i, step)
		         
