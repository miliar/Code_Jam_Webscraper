t = int(raw_input())

for i in xrange(1, t + 1):
    num = [int(c) for c in raw_input()]
    segment_start = 0
    for j in xrange(1, len(num)):
        if num[j] < num[j-1]:
            num[segment_start] -= 1
            for q in xrange(segment_start + 1, len(num)):
                num[q] = 9
        if num[j] != num[j-1]:
            segment_start = j

    answer = "".join([str(c) for c in num]).lstrip("0")
    print "Case #{}: {}".format(i, answer)
