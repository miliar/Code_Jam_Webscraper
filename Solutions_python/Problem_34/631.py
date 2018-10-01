import re


with open('D:\A-large.in') as f:
	with open('D:\A-large.out','w') as of:
		line = f.readline()
		line = line.strip()
		li = line.split()
		L = int(li[0])
		D = int(li[1])
		N = int(li[2])
		words = []
		for i in range(0, D):
			words.append(f.readline().strip())
	
		for i in range(0, N):
			line = f.readline()
			line = line.strip()
			line = line.replace('(','[')
			line = line.replace(')',']')
			
			p = re.compile(line)
			count = 0
			for j in range(0, D):
				if p.match(words[j]):
					count += 1
			of.write("Case #" + str(i + 1) + ": " + str(count) + "\n")