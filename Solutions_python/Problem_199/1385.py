t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
    flip_counter = 0
    sequence, k = [s for s in raw_input().split(" ")]
    k = int(k)
    sequence = list(sequence)
    for j in range(0, len(sequence)+(1-k)):
        if sequence[j] == '-':
            flip_counter += 1
            sequence[j] = '+'
            #then reverse next k-1
            for l in range(1,k):
                if sequence[j+l] == '+':
                    sequence[j+l] = '-'
                else:
                    sequence[j+l] = '+'
    for j in range(len(sequence)+(1-k),len(sequence)):
        if sequence[j] == '-':
            flip_counter = 'IMPOSSIBLE'

    print "Case #{}: {}".format(i, flip_counter)
  # check out .format's specification for more formatting options