import re

def self():
	t = int(sys.stdin.readline())
	i = 0
	while i<t:
		i = i+1
		print "Case #"+str(i)+":",
		n = int(sys.stdin.readline())

		wires = []		

		j = 0
		count = 0
		while j<n:
			line = sys.stdin.readline()
			wires.append(line.split())
			j = j+1

		j = 0
		while j<n:
			k = j + 1
			while k < n:
				if int(wires[j][0])>int(wires[k][0]) and int(wires[j][1])<int(wires[k][1]):
					count = count+1
				elif int(wires[j][0])<int(wires[k][0]) and int(wires[j][1])>int(wires[k][1]):
					count = count+1
				k = k+1
			j = j+1
		print(count)
	

if __name__ == "__main__":
	import sys
	self()
