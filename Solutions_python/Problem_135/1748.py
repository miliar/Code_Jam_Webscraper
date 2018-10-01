input = open('A-small-attempt0.in', 'r')
output = open('A-small-attempt0.out', 'w')

test_count = input.readline()

for i in range(0, int(test_count)):
    candidates = []
    for j in range(0, 2):
        line_number = int(input.readline())
        lines = []
        candidate_set = []
        for k in range(0, 4):
            lines.append(input.readline().rstrip())
        candidates_str = lines[line_number - 1].split(' ')
        for s in candidates_str:
            candidate_set.append(int(s))
        candidates.append(candidate_set)
    print candidates
    equal_count = 0
    for n in candidates[0]:
        for m in candidates[1]:
            if(n == m):
                print str(n) + ", " + str(m)
                equal_number = n
                equal_count += 1
    print equal_count
    output.write("Case #" + str(i + 1) + ": ")
    if(equal_count == 0):
        output.write("Volunteer cheated!\n")
    elif(equal_count == 1):
        output.write(str(equal_number) + "\n")
    else:
        output.write("Bad magician!\n")

input.close()
output.close()
