fin = open("C-small.in", 'r');
fout = open("C-small.out", 'w');

caseNum = int(fin.readline());

for case in range(caseNum):
    a, b = fin.readline().split();
    i = int(a);
    j = int(b);
    r = 0;
    check = [];
    for n in range(i, j+1):
	move = len(str(n)) - 1;
	while move > 0:
            m = int(str(n)[move:] + str(n)[:move]);
	    if ((n, m) not in check) and ((m, n) not in check) and (m >= i) and (m <= j) and (m != n):
	        r += 1;
		check.append((n, m));
	    move -= 1;
    fout.write("Case #" + str(case+1) + ": " + str(r) + '\n');

fin.close();
fout.close();


