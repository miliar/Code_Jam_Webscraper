def read_input_file(filename = "A-small-attempt0.in"):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    N = int(lines[0])
    cases = []
    for line in lines[1:]:
        cases.append(line)
    return N, cases

T, cases = read_input_file('B-large.in')

results = []

for case in cases:
    case = case.split()
    N = int(case[0])
    S = int(case[1])
    p = int(case[2])
    scores = []
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    for score in case[3:]:
        scores.append(int(score))
    for score in scores:
        if 3*p-2 <= score:
            count1 += 1
            print score, 'close'
        elif 0 <= 3*p-4 <= score:
            count2 += 1
            print score, 'suprise'
    results.append(count1 + (count2 if count2 < S else S))

def create_output(filename = "B_large_solution.txt"):
    file = open(filename, 'w')
    for i in range(len(cases)):
        print "Case #%d: %s" % (i+1, results[i])
        output = "Case #%d: %s\n" % (i+1, results[i])
        file.write(output)
    file.close()

create_output()

