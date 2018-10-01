import sys

cases = int(raw_input())

test_list = []
cases_list =[]
for i in xrange(cases) : 
	test_list.append(map(str, raw_input().split()))

cases_list = map(lambda i: (i + 1, int(test_list[i][0]), [int(s) for s in test_list[i][1]] ) , range(len(test_list)))

for case in cases_list :
	maxS = int(case[1])
	friends = 0
	people_applaud = case[2][0]
	for shiness in xrange(1, maxS + 1):
		people_not_applaud = case[2][shiness]

		if((shiness - people_applaud) >= 0):
			result = shiness - people_applaud
			friends += result
			people_applaud += result
		
		people_applaud += people_not_applaud

	print "CASE #{0}: {1}".format(case[0], friends)
