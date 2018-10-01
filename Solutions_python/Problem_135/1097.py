import sys

basename = "A-small-attempt0"

input_filename = basename + ".in"
output_filename = basename + ".out"

input_file = open(input_filename, 'r')
output_file = open(output_filename, 'w')

test_cases = int(input_file.readline().rstrip())

for case in range(1, test_cases+1):
    rownum1 = int(input_file.readline().rstrip())
    cards1 = []
    for i in range(4):
        line = [int(j) for j in input_file.readline().rstrip().split(' ')]
        cards1.append(line)
    rownum2 = int(input_file.readline().rstrip())
    cards2 = []
    for i in range(4):
        line = [int(j) for j in input_file.readline().rstrip().split(' ')]
        cards2.append(line)
    
    options = [i for i in cards1[rownum1 - 1] if i in cards2[rownum2 - 1]]

    if len(options) == 1:
        solution = str(options[0])
    elif len(options) == 0:
        solution = "Volunteer cheated!"
    else:
        solution = "Bad magician!"
    
    # Output all goes below here. Make sure to define var 'solution' 
    output_file.write("Case #" + str(case) + ": " + str(solution))
    if case < test_cases:
        output_file.write('\n')

