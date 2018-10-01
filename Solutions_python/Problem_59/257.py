inp = open('test.in', 'r');
out = open('test.out', 'w');
t = int(inp.readline().strip())

def solve(test):
	nm = inp.readline().strip().split()
	(n,m) = ( int(nm[0]), int(nm[1]) );
	dirs = set();
	for i in range(n) :
		path = inp.readline().strip(' /	\n')
#		print path
		dirs.add( path );

	ans = 0;
	for i in range(m) :
		path = inp.readline().strip(' /	\n').split('/')
#		print path
		parent = '';
		for p in path :
			t = parent+p;
			if not ( t in dirs ) :
				dirs.add(t);
				ans += 1;
			parent = t+'/';
	out.write("Case #%d: %d\n" % (test, ans))
#	print "\n\n\n"

for i in range(t): solve(i+1)
