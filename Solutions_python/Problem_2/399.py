import sys

def readnumber(fd):
	str = fd.readline()
	split = str.split()
	na = int(split[0])
	nb = int(split[1])
	return na, nb

def convtime(str):
	split = str.split(':')
	return int(split[0]) * 60 + int(split[1])
	
def readtime(fd, n):
	list = []
	for i in range(n):
		str = fd.readline()
		split = str.split()
		v = [convtime(split[0]), convtime(split[1]), 1]
		list.append(v)
	return list

def ArrivalKey(v):
	return v[1];

def LeaveKey(v):
	return v[0];

def main():
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	
	ifd = open(input_file, 'r')
	ofd = open(output_file, 'w')
	
	# cases
	N = int(ifd.readline())
	
	for n in range(N):
		turnaround = int (ifd.readline())
		na, nb = readnumber(ifd)
		aList = readtime(ifd, na)
		bList = readtime(ifd, nb)
		
		# Mark A
		bList.sort(key=ArrivalKey)
		aList.sort(key=LeaveKey)
		
		for b in bList:
			arrivalTime = b[1]
			for a in aList:
				leaveTime = a[0]
				mark = a[2]
				if ((leaveTime >= arrivalTime + turnaround) and (mark == 1)):
					a[2] = 0
					break;
		
		# Mark B
		bList.sort(key=LeaveKey)
		aList.sort(key=ArrivalKey)
		
		for a in aList:
			arrivalTime = a[1]
			for b in bList:
				leaveTime = b[0]
				mark = b[2]
				if ((leaveTime >= arrivalTime + turnaround) and (mark == 1)):
					b[2] = 0
					break;
		
		na = 0
		nb = 0
		for a in aList:
			if (a[2]): na += 1
		for b in bList:
			if (b[2]): nb += 1
		ofd.write("Case #%d: %d %d\n" % (n + 1, na, nb))

	ifd.close()
	ofd.close()
	
	
main()