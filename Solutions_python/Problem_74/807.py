import os
import sys
from collections import deque

#s = "4 O 2 B 1 B 2 O 4"
#s = "3 O 5 O 8 B 100"
#s = "2 B 2 B 1"

def calculate(s):
	o_values = []
	b_values = []
	toks = s.split(" ")
	count = int(toks[0])

	i = 1
	j = 0
	while(j < count):
		type = toks[i]
		button = int(toks[i+1])

		if(type == "O"):
			o_values.append(button)
		else:
			b_values.append(button)

		j = j + 1
		i = i + 2


	queue = deque(toks)
	count = int(queue.popleft())

	sec = 0
	bi = 0
	oi = 0
	bpos = 1
	opos = 1
	b_value = 1
	o_value = 1
	for i in range(count):
		type = queue.popleft()
		button = queue.popleft()

		if(bi < len(b_values)):
			b_value = b_values[bi]

		if(oi < len(o_values)):
			o_value = o_values[oi]

		if(type == "B"):
			while(bpos < b_value):
				bpos = bpos + 1
				sec = sec + 1
				if(opos < o_value):
					opos = opos + 1
				if(opos > o_value):
					opos = opos - 1

			while(bpos > b_value):
				bpos = bpos - 1
				sec = sec + 1
				if(opos < o_value):
					opos = opos + 1
				if(opos > o_value):
					opos = opos - 1

			sec = sec + 1
			if(opos < o_value):
				opos = opos + 1
			if(opos > o_value):
				opos = opos - 1
			bi = bi + 1
		else:	
			#print str(opos)+"\t"+str(o_value)
			while(opos < o_value):
				opos = opos + 1
				sec = sec + 1
				if(bpos < b_value):
					bpos = bpos + 1
				if(bpos > b_value):
					bpos = bpos - 1

			while(opos > o_value):
				opos = opos - 1
				sec = sec + 1
				if(bpos < b_value):
					bpos = bpos + 1
				if(bpos > b_value):
					bpos = bpos - 1
			
			sec = sec + 1
			if(bpos < b_value):
				bpos = bpos + 1
			if(bpos > b_value):
				bpos = bpos - 1
			oi = oi + 1

	return sec

first = True
i = 1
for line in sys.stdin:
	line = line.rstrip("\n")
	if(first):
		count = int(line)
		first = False
		continue
	print "Case #"+str(i)+": "+str(calculate(line))
	i = i + 1

