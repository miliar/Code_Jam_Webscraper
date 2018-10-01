f = open('A-small-attempt0.in', 'r')
o = open('output', 'w')
t = f.readline().rstrip()
for i in range(0,int(t)):
    a1 = int(f.readline().rstrip())
    for j in range(1,5):
        if j == a1:
            r1 = set(f.readline().rstrip().split())
        else:
            f.readline()
    a2 = int(f.readline().rstrip())
    for j in range(1,5):
        if j == a2:
            r2 = set(f.readline().rstrip().split())
        else:
            f.readline()
    result = list(r1.intersection(r2))
    r = len(result)
    if r == 0:
        o.write('Case #' + str(i+1) + ': Volunteer cheated!\n')
    elif r == 1:
        o.write('Case #' + str(i+1) + ': ' + result[0] + '\n')
    else:
        o.write('Case #' + str(i+1) + ': Bad magician!\n')
f.close()
o.close()
