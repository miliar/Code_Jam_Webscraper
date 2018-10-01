num_test_cases = int(raw_input())


for j in xrange(1, num_test_cases + 1):
    config_1 = []
    config_2 = []
    guess_1 = int(raw_input()) - 1
    for i in xrange(4):
        config_1.append(raw_input().split())
    guess_2 = int(raw_input()) - 1
    for i in xrange(4):
        config_2.append(raw_input().split())

    intersection = set.intersection(set(config_1[guess_1]),set(config_2[guess_2]))
    ans = len(intersection)
    if ans == 1:
        print "Case #" + str(j) + ": " + list(intersection)[0]
    elif ans == 0:
        print "Case #" + str(j) + ": " + "Volunteer cheated!"
    else:
        print "Case #" + str(j) + ": " + "Bad magician!"

