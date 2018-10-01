def is_circle_pair(inta,b):
    a = str(inta)
    for i in range(len(a)-1):
	ca = int(a[i+1:]+a[0:i+1])
	if ca==b: 
	    return True
    return False

fn = 'C-small-attempt0'
fi = open('%s.in' % fn, 'r')
fo = open('%s.out' % fn, 'w')
t = int(fi.readline())
cases = fi.readlines()
fi.close()

for c in range(t):
    [a,b] = map(lambda x:int(x), cases[c].strip().split(' '))
    count = 0
    for x in range(a,b+1):
	for y in range(x+1,b+1):
	    if is_circle_pair(x,y):
		count = count + 1
    fo.write('Case #%s: %s\n' % ((c+1), count))

fo.close()
