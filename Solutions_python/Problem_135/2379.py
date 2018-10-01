import sys
lines = [line for line in sys.stdin]
test_cases = int(lines[0])
index = 1

for test in xrange(test_cases):
    real_answer = None
    diff = None

    first_answer = int(lines[index])
    first_row = [int(x) for x in lines[index+1].split(' ')]
    second_row = [int(x) for x in lines[index+2].split(' ')]
    third_row = [int(x) for x in lines[index+3].split(' ')]
    fourth_row = [int(x) for x in lines[index+4].split(' ')]

    if first_answer == 1:
        real_answer = set(first_row)
    elif first_answer == 2:
        real_answer = set(second_row)
    elif first_answer == 3:
        real_answer = set(third_row)
    elif first_answer == 4:
        real_answer = set(fourth_row)

    second_answer = int(lines[index + 5])
    first_row = [int(x) for x in lines[index+6].split(' ')]
    second_row = [int(x) for x in lines[index+7].split(' ')]
    third_row = [int(x) for x in lines[index+8].split(' ')]
    fourth_row = [int(x) for x in lines[index+9].split(' ')]

    if second_answer == 1:
       diff = real_answer & set(first_row)
    elif second_answer == 2:
        diff = real_answer & set(second_row)
    elif second_answer == 3:
       diff = real_answer &  set(third_row)
    elif second_answer == 4:
        diff = real_answer & set(fourth_row)

    if len(diff) == 1:
        print "Case #%s: %s" % (test+1, diff.pop())
    elif len(diff) > 1:
        print "Case #%s: Bad magician!" % (test+1)
    else:
        print "Case #%s: Volunteer cheated!" % (test+1)
    index += 10







