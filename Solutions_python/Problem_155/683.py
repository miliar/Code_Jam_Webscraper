import collections

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

f = [i for i in open('A-large.in')]
f[-1] +='\n'
data = [i[:-1] for i in f]
cases = []
for i in range(int(data[0])):
	people = data[i+1].split(' ')
	print(people)
	standing = int(people[1][0])
	added = 0
	for j in range(1, int(people[0])+1):
		print('variant', j, standing)
		if j>standing:
			added+= j-standing
			standing += j-standing
		standing += int(people[1][j])
	cases.append('Case #'+str(i+1)+': '+str(added))
print(cases)
f1 = open('output.txt','w')
[f1.write(i+'\n') for i in cases]