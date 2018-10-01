def oviation(max_level,audience):
	if max_level == 0:
		return 0
	result = [0]*max_level
	for i in range(1,max_level+1):
		result[i-1] = i
		for j in range(i):
			result[i-1] -= int(audience[j])
		result[i-1] = max(result[i-1],0)

	return max(result)

if __name__ == '__main__':
	f = open('A-large.in','r')
	r = open('oviation_result.txt','w')
	test = int(f.readline())
	for i in range(test):
		max_level,audience = f.readline().split(' ')
		result = oviation(int(max_level),audience)
		r.write('Case #%s: %s' %(i+1,result))
		if i != test-1:
			r.write('\n')
	r.close()
	f.close()