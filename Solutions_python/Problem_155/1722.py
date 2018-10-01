input_file = open('a-large.txt')
input_file.readline()
for input_num, line in enumerate(input_file):
    _, levels = line.strip().split(' ')
    levels = [int(c) for c in levels]
    friends = 0
    total = 0
    for level, people in enumerate(levels):
        if level > total:
            friends += (level - total)
            total += (level - total)
        total += people
    print "Case #{}: {}".format(input_num + 1, friends)
