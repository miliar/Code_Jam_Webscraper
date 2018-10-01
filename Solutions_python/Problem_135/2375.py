T = int(raw_input())

for x in range(T):
    ans1 = int(raw_input())
    arr1 = []
    for i in range(4):
        line = raw_input()
        arr1.append([int(a) for a in line.split()])
    ans2 = int(raw_input())
    arr2 = []
    for i in range(4):
        line = raw_input()
        arr2.append([int(a) for a in line.split()])
    answer = list(set(arr1[ans1-1]) & set(arr2[ans2-1]))
    if len(answer) > 1:
        print "Case #{0}: {1}".format(x+1, "Bad magician!")
    elif len(answer) == 0:
        print "Case #{0}: {1}".format(x+1,"Volunteer cheated!")
    else:
        print "Case #{0}: {1}".format(x+1,answer[0])
