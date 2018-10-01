fo = open("A-small-attempt2.in", "r")
f = open('output.out', 'w')
n = int(fo.readline())
r={}
for i in range(n):
    r1 = {};
    r2 = {};
    a1 = int(fo.readline())
    for j in range(4):
        r1[j] = fo.readline().split()
    a2 = int(fo.readline())
    for j in range(4):
        r2[j] = fo.readline().split()
    l1 = r1[a1-1]
    l2 = r2[a2-1]
    r[i]=set(l1)&set(l2)
for i in range(n):
    if len(r[i]) == 1:
        f.write("Case #"+str((i+1))+": "+next(iter(r[i]))+"\n")
    elif len(r[i]) > 1:
        f.write("Case #"+str((i+1))+": Bad magician!\n")
    else:
        f.write("Case #"+str((i+1))+": Volunteer cheated!\n")
f.close()
fo.close()
