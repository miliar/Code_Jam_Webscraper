fname = 'A-small-attempt1.in'
with open(fname) as f:
    Data = f.read().splitlines()
data = []
for i in Data:
    data.append([int(j) for j in i.split()]) if len(i) > 1 else data.append(int(i))
NumCases = data[0][0]
del data[0]
Cases = []
n,m = 10,0
for i in xrange(NumCases):
    Cases.append(data[m:n])
    n += 10
    m += 10
C = 1
while Cases:
    count, card = 0, None
    Row1,Row2 = None,None
    i = Cases.pop(0)
    Row1 = i[i[0]]
    Row2 = i[5+i[5]]
    for j in xrange(4):
        for k in xrange(4):
            if Row1[j] == Row2[k]:
                count += 1
                card = Row1[j]
    if count > 1:
        print "Case #" + str(C) + ": Bad magician!"
    elif count == 1:
        print "Case #" + str(C) + ": " + str(card)
    elif count == 0:
        print "Case #" + str(C) + ": Volunteer cheated!"
    C += 1