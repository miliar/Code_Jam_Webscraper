#!/usr/bin/python

case_count = int(raw_input());

for i in range(0, case_count):
	print 'Case #' + str(i+1) + ':',;
	rkn = raw_input().split(' ');
	r_val = int(rkn[0]);
	k_val = int(rkn[1]);
	n_val = int(rkn[2]);
	groups = raw_input().split(' ');
	for j in range(0, len(groups)):
		groups[j] = int(groups[j]);
	earn = 0;
	for j in range(0, r_val):
		board = 0;
		humans = 0;
		while True:
			if groups[0] + board <= k_val and humans < n_val:
				board += groups[0];
				groups.append(groups[0]);
				groups = groups[1:];
				humans += 1;
			else:
				break;
		earn += board;
	print earn;
