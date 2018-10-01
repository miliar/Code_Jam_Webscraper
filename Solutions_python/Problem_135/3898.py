file = open('A-small-attempt3.in', 'r')
out = open('magic-output.in', 'r+')
t = int(file.readline())
for i in range(t):
    x1 = int(file.readline())
    f1, f2, f3, f4 = [], [], [], []
    f1 = file.readline().split()
    f2 = file.readline().split()
    f3 = file.readline().split()
    f4 = file.readline().split()
    for j in range(4):
        f1[j] = int(f1[j])
        f2[j] = int(f2[j])
        f3[j] = int(f3[j])
        f4[j] = int(f4[j])
    cards1 = []
    cards1 = [f1, f2, f3, f4]
    x2 = int(file.readline())
    s1, s2, s3, s4 = [], [], [], []
    s1 = file.readline().split()
    s2 = file.readline().split()
    s3 = file.readline().split()
    s4 = file.readline().split()
    for j in range(4):
        s1[j] = int(s1[j])
        s2[j] = int(s2[j])
        s3[j] = int(s3[j])
        s4[j] = int(s4[j])
    cards2 = []
    cards2 = [s1, s2, s3, s4]
    choice1, choice2 = [], []
    choice1 = cards1[x1 - 1]
    choice2 = cards2[x2 - 1]
    choice1 = sorted(choice1)
    choice2 = sorted(choice2)
    count = 0
    for l in range(4):
        for k in range(4):
            if(choice1[l] == choice2[k]):
                count = count + 1
    if(count == 1):
        for l in range(4):
            for k in range(4):
                if(choice1[l] == choice2[k]):
                    temp = l
        out.write('Case #' + str(i + 1) + ': ' + str(choice1[temp]) + '\n')
    elif(count == 0):
        out.write('Case #' + str(i + 1) + ': Volunteer cheated!\n')
    else:
        out.write('Case #' + str(i + 1) + ': Bad magician!\n')
file.close()
out.close()
