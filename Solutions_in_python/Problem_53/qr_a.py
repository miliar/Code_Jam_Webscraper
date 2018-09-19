#!/usr/bin/python

case_count = int(raw_input());

for i in range(0, case_count):
	print 'Case #' + str(i+1) + ':',;
	nk_slist = raw_input().split(' ');
	nk_list = [];
	for j in range(0, len(nk_slist)):
		nk_list.append(int(nk_slist[j]));
	if nk_list[1] & (2**nk_list[0]-1) == (2**nk_list[0]-1):
		print 'ON';
	else:
		print 'OFF';
