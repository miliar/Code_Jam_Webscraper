import sys

finput = sys.argv[1]
fi = open(finput)
num = int(fi.readline())

def f2(seq): 
	checked = []
	for e in seq:
		if e not in checked:
    			checked.append(e)
	return checked

def include(ex, new):
	i = 0
	for pos in range(min(len(new), len(ex))):
		if new[pos] == ex[pos]:
			i += 1
		else:
			break

	return i

def process(exist, create):
	mkdir = 0
	for path in create:
		ma = 0
		for ex in exist:
			ma = max(ma, include(ex, path))
		if ma < len(path):
			mkdir += len(path) - ma
		for i in range(ma, len(path)):
			exist += [path]
	return mkdir

for i in range(num):
	case = fi.readline().strip("\n").split()
	exist = []
	create = []
	for j in range(int(case[0])):
		new = fi.readline().strip("\n").split("/")[1:]
		for k in range(1, len(new)+1):
			exist += [new[:k]]
	for j in range(int(case[1])):
		new = fi.readline().strip("\n").split("/")[1:]
		for k in range(1, len(new)+1):
			create += [new[:k]]
	exist = f2(exist)
	exist.sort()
	create = f2(create)
	create.sort()
	
	print ("Case #%i: %i") % (i+1, process(exist, create))
