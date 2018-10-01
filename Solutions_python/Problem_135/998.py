input = open('input1', 'r')
output = open('output1', 'w')

testcases = int(input.readline().strip())
for testcase in xrange(1, testcases+1):
    first_ans = int(input.readline().strip())
    for row in xrange(4):
        r = input.readline()
        if row == first_ans - 1:
            sol_list = r
    sol_list = sol_list.strip().split(' ')
    second_ans = int(input.readline().strip())
    for row in xrange(4):
        r = input.readline()
        if row == second_ans - 1:
            sol = r
    sol = sol.strip().split(' ')
    result = [x for x in sol if x in sol_list]
    if len(result) == 0:
        output.write("Case #%s: Volunteer cheated!\n" % testcase)
    elif len(result) > 1:
        output.write("Case #%s: Bad magician!\n" % testcase)
    else:
        output.write("Case #%s: %s\n" % (testcase, result[0]))
    

input.close()
output.close()
