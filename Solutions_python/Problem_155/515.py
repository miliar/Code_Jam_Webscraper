import sys

cases = int(raw_input())

for current_case in range(1, cases+1):
	Smax = raw_input().split()
	Smax, S = int(Smax[0]), Smax[1]
	
	standing = 0
	added = 0
	for k in range(0, Smax+1):
		if standing < k:
			added += 1
			standing += 1
		standing += int(S[k])
	
	print "Case #%d: %d" % (current_case, added)