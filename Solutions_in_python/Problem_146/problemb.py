import math

def removeDupes(trains):
    t = trains[:]
    arr = []
    for i in range(len(t)):
	a = t[i][0]
	s = a
	for j in range(len(t[i])):
	    if t[i][j] != a:
		a = t[i][j]
	    	s = s + a
	arr.append(s)
    return arr

def checkInternal(trains):
    for i in range(len(trains)):
	t = trains[i]
	if len(t) >= 3:
	    for q in t[1:-1]:
		for s in range(len(trains)):
		    if s != i and q in trains[s]:
			return -1
	    f = t.find(q)
	    s = t.find(q, f+1)
	    if s != -1 and s != (len(t)-1):
		return -1
    return 1

def removeOnlyOne(trains):
    letters = 'qwertyuioplkjhgfdsazxcvbnm'
    total = 1
    final = trains[:]
    for i in range(len(letters)):
	same = []
	notSame = []
	for j in final:
	    n = 1
	    for k in j:
		if k == letters[i]:
		    pass
		else:
		    n = 0
		    notSame.append(j)
		    break
	    if n == 1:
		same.append(j)
	if len(same) >= 2:
	    total *= math.factorial(len(same))
	    final = notSame[:] + [letters[i]]
    return final, total

def joinStuff(trains, px):
    total = px
    letters = 'qwertyuioplkjhgfdsazxcvbnm'
    final = trains[:]
    for i in letters:
	starting, ending, ones = [], [], []
	for f in range(len(final)):
	    if len(final[f]) == 1:
		if final[f] == i:
		    ones.append(f)
	    else:
		if final[f][0] == final[f][-1]:
		    return [-1, -1]
		if final[f][0] == i:
		    starting.append(f)
		if final[f][-1] == i:
		    ending.append(f)
	if len(ones) > 1 or len(starting) > 1 or len(ending) > 1:
	    return [-1, -1]
	else:
	    if len(starting) == 1 and len(ending) == 1:
		temp = final[ending[0]] + final[starting[0]][1:]
		final2 = [temp]
		for b in range(len(final)):
		    if b != starting[0] and b != ending[0]:
			final2.append(final[b])
		if len(ones) == 1:
		    final2.remove(final[ones[0]])
		final = final2[:]
	    elif len(starting) == 1 and len(ones) == 1:
		final.remove(final[ones[0]])
	    elif len(ending) == 1 and len(ones) == 1:
		final.remove(final[ones[0]])
    return [final, px]

def func(trains):
    #print trains
    t = removeDupes(trains)
    #print t
    if checkInternal(t) == -1:
	return -1
    [t2, p] = removeOnlyOne(t)
    #print 't2', t2, p
    [t3, p] = joinStuff(t2, p)
    #print 't3', t3, p
    if p == -1:
	return -1
    p *= math.factorial(len(t3))
    print t3, p
    #print t3, p
    return p


f = open('B-small-attempt6.in', 'r')
fw = open('output.out', 'w')

r = f.readline()
for i in range(int(r)):
    r = f.readline()
    r = f.readline().replace('\n', '').split(' ')
    val = func(r)
    if val == -1:
	val = 0
    fw.write('Case #' + str(i+1) + ': ' + str(val) + "\n")
    print i

