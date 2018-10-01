kases = input();

from sets import Set

for kk in range(kases):

	x = raw_input();
	y = Set(x);

	base = max(2,len(y));

	dict = {};
	t = 0;
	dict[x[0]] = 1;
	for i in xrange(1,len(x)):
		if(not dict.has_key(x[i])):
			dict[x[i]] = t;
			t += 1;
			if(t == 1): t += 1;
	
	l = len(x) - 1;
	ans = 0;t = 0;
	while (l >= 0 ):
		ans += dict[x[l]] * (base ** t);
		t += 1;
		l -= 1;
	
	print "Case #" + (str )(kk + 1) + ": " + (str )(ans);
