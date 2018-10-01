from sys import stdin
# 4
# 4 11111
# 1 09
# 5 110011
# 0 1


TCs = int(stdin.readline())
for t in range(TCs):
	line = stdin.readline()
	line = str.split(line, " ")
	shyness = int(line [0])
	audience = line[1].strip()
	ovation = 0
	extra_friends = 0
	for k, aud_per_k in enumerate (audience) :
		
		if k == 0 or aud_per_k == 0:
			ovation += int(aud_per_k)
			continue

		# if ovation >= k then add aud_per_k to the ovation and continue
		# else add (k-ovation) to the extra friends, add the value to ovation then add aud_per_k
		if ovation < k :
			missing = k-ovation
			extra_friends+=missing
			ovation += missing

		ovation += int(aud_per_k)
	print "Case #" + str(t+1) +": "+ str(extra_friends)