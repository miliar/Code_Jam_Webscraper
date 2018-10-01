input_file = open("A-small-attempt0.in")

num_t = int(input_file.readline())

for t in xrange(num_t):
    candidates = []

    for i in xrange(2):
        row_index = int(input_file.readline())

        mat = []

        for r in xrange(4):
            mat.append(input_file.readline())

        candidates.append({int(s) for s in mat[row_index - 1].split(' ')})

    can_has_result = set.intersection(candidates[0], candidates[1])

    if (len(can_has_result) == 1):
        result = list(can_has_result)[0]
    elif (len(can_has_result) == 0):
        result = 'Volunteer cheated!'
    else:
        result = 'Bad magician!'

    print 'Case #' + str(t + 1) + ': ' + str(result)