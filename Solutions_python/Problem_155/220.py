import re
import sys
buf=[]
def scans():
    global buf
    while 1:
        while len(buf) <= 0:
            buf=input().replace('\n',' ').split(' ')
        o=buf.pop(0)
        if o!='':
            break
    return o
def scan():
    return int(scans())

sys.stdin = open('input.txt')
ofg=1
if ofg:
	sys.stdout = open('output.txt','w')
for t in range(scan()):
	out = 0
	standing = 0
	n = scan()
	arr = [int(i) for i in scans().strip()]
	if len(arr) != n+1:
		sys.stderr.write('???\n')
	for k,i in enumerate(arr):
		if standing < k:
			out+=k-standing
			standing+=k-standing
		standing+=i
	print('Case #%d: %d'%(t+1,out))
if ofg:
	sys.stdout.flush()
	sys.stdout.close()