f_in = open('A-large.in', 'r')
f_out = open('A-large.out', 'w')

test_num = f_in.readline()
print(test_num)
lines = f_in.readlines()

for index, line in enumerate(lines):
    answer = 0
    max_shyness, tmp = line.split(' ')
    audiences = [int(n) for n in list(tmp.strip('\n'))]
    print(max_shyness, audiences)
    standing = audiences[0]
    no_standing = audiences[1:]

    judges = []
    shyness = int(max_shyness)
    for i in range(0, len(no_standing)):
        no_standing.pop()
        judge = shyness - (int(standing) + sum(no_standing))
        shyness -= 1
        judges.append(judge)

    print(judges)
    if judges:
        answer = max(judges)
        if answer < 0:
            answer = 0
    else:
        answer = 0
    print(answer)

    out = "Case #%d: %d\n" % (index + 1, answer)
    f_out.write(out)
