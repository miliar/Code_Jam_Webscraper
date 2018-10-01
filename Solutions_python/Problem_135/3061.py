import sys

def func():
	a=input()
	a-=1
	for i in range(4):
		if i==a:
			t = sys.stdin.readline().rstrip().split(" ")
		else:
			sys.stdin.readline()
			pass
	return t

tt=input()
for i in range(tt):
	x = func()
	y = func()
	r = [val for val in x if val in y]
	sys.stdout.write("Case #%d: " % (i+1))
	if len(r) == 1:
		print r[0]
	elif len(r) > 1:
		print "Bad magician!"
	else:
		print "Volunteer cheated!"

