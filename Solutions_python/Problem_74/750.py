infile = open('bottrust.in')
outfile = open('bottrust.out', 'w')

T = int(infile.readline().strip())

for i in xrange(T):
    instructions = infile.readline().strip().split()
    N = int(instructions[0])
    instructions = instructions[1:]

    cur_color = instructions[0]
    o_pos, b_pos = 1, 1
    cost = 0
    surplus = 0

    while instructions:
        color, pos = instructions[0], int(instructions[1])
        instructions = instructions[2:]
        if cur_color == color:
            dist = abs((o_pos if color == 'O' else b_pos) - pos)
            cost += 1 + dist
            surplus += 1 + dist
        else:
            dist = abs((o_pos if color == 'O' else b_pos) - pos)
            cost += 1 + max(0, dist - surplus)
            surplus = 1 + max(0, dist - surplus)
            cur_color = color
        if color == 'O':
            o_pos = pos
        else:
            b_pos = pos

    outfile.write('Case #%d: %d\n' % (i + 1, cost))
