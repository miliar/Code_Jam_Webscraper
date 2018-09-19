import sys

in_file = open(sys.argv[1])

num_test_cases = int(in_file.readline().strip())

for i in range(num_test_cases):
    entry = in_file.readline().strip().split(' ')
    entry = [int(x) for x in entry]
    num_googs = entry.pop(0)
    num_surprises = entry.pop(0)
    target_score = entry.pop(0)
    min_score = 3 * target_score - 2
    min_surprise_score = 3 * target_score - 4

    if target_score == 1:
        min_score = 1
        min_surprise_score = 1

    p = 0

    for j in range(num_googs):
        if entry[j] >= min_score:
            p += 1
        elif entry[j] >= min_surprise_score and num_surprises:
            p += 1
            num_surprises -= 1

    print "Case #%s: %s" % (i+1, p)



