import sys,math

cases = int(raw_input())
rows = []

for i in range(cases*2):
    answer = raw_input()
    #print answer
    rows.append([])
    for j in range(4):
        if j+1 == int(answer):
            a = raw_input()
            rows[int(math.floor(i/2))].append(a)
        else:
            a = raw_input()

for i in range(cases):
    #print rows
    solutions = []
    rows1 = rows[i][0].split(' ')
    rows2 = rows[i][1].split(' ')
    for j in range(4):
        for k in range(4):
            if rows1[k] == rows2[j]: 
                solutions.append(rows1[k])
    if len(solutions) == 0:
        print "Case #"+str(i+1)+": " + "Volunteer cheated!"
    elif len(solutions) == 1:
        print "Case #"+str(i+1)+": " + solutions[0]
    elif len(solutions) > 1:
        print "Case #"+str(i+1)+": " + "Bad magician!"
