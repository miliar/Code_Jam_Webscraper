# Candy Splitting
# Google Code Jam
# Ameer Ayoub <ameer.ayoub@gmail.com>
# 1:31am 5/6/2011

import math
global_max_pile = -1

def CalcDifference(l1, l2):
	if reduce(lambda x, y: x^y, l1) == reduce(lambda x, y: x^y, l2):
		return max(sum(l1), sum(l2))
	else:
		return -1

def FindMaxCandySplit(l1, l2, remaining):
	global global_max_pile
	if(not remaining):
		if((l1 and l2) and (len(l1) >= len(l2))):
			pile = CalcDifference(l1, l2)
			#print l1, l2, pile
			if pile > global_max_pile:
				global_max_pile = pile
	else:
		l1.append(remaining[0])
		FindMaxCandySplit(l1[:], l2[:], remaining[1:])
		l1 = l1[:-1]
		l2.append(remaining[0])
		FindMaxCandySplit(l1[:], l2[:], remaining[1:])

def CandyEntryPoint(l):
	global global_max_pile
	global_max_pile = -1
	FindMaxCandySplit([], [], l)
	if (global_max_pile != -1):
		return str(global_max_pile)
	else:
		return "NO"
	

def TestCandy():
	global global_max_pile
	global_max_pile = -1
	#FindMaxCandySplit([], [], [511095, 869762, 636418, 501890, 125885, 994784, 577107, 866127, 188104, 253234, 379765, 288840, 273951, 981232, 384540])
	FindMaxCandySplit([], [], [9857, 7757])
	print "Test Case:",
	if (global_max_pile != -1):
		print global_max_pile
	else:
		print "NO"
		
def ExecuteCandy():
	f = open("candy.in")
	o = open("candy.out", "w")
	num_cases = 0
	i = 0
	line = f.readline()
	if(line):
		num_cases = int(line)
	while(i < num_cases):
		line = f.readline()
		num_candy = int(line)
		line = f.readline()
		split_line = map(int, line.split(' '))
		if len(split_line) > num_candy:
			split_line = split_line[:num_candy]
		o.write("Case #"+str(i+1)+": "+CandyEntryPoint(split_line)+"\n")
		i += 1

if __name__ == "__main__":
	#TestCandy()
	ExecuteCandy()