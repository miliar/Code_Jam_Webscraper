filename = 'A-large.in'
f = open(filename)
T = int(f.readline().split()[0])
cases = []
for _ in range(T):
    line = f.readline().split()
    smax = int(line[0])
    shyness = line[1]
    cases.append([smax, shyness])
f.close()
answers = []
for case in cases:
    invited = 0
    standing = 0
    for shylevel in range(case[0]+1):
        n = int(case[1][shylevel])
        if shylevel > standing:
            invite = shylevel - standing
            invited += invite
            standing+= invite
        standing += n
    answers.append(invited)
filename = 'output.txt'
f = open(filename, mode='w')
for index, ans in enumerate(answers):
    s = 'Case #' + str(index+1) + ': ' + str(ans)
    print(s)
    f.write(s+ '\n')
f.close()
