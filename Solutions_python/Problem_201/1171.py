#f_in = open('C.in', 'r')
#f_in = open('C-small-1-attempt0.in', 'r')
f_in = open('C-small-2-attempt0.in', 'r')
#f_in = open('C-large.in', 'r')
#f_out = open('C.out', 'w')
#f_out = open('C-small-1.out', 'w')
f_out = open('C-small-2.out', 'w')
#f_out = open('C-large.out', 'w')

T = int(f_in.readline())

for t in xrange(1, T+1):
    line_list = f_in.readline()[:-1].split(" ")
    N = int(line_list[0])
    K = int(line_list[1])

    values = [N]
    sizes = [1]

    for i in xrange(K - 1):
        val1 = values[0] / 2
        if val1 in values:
            sizes[values.index(val1)] += 1
        else:
            values.append(val1)
            sizes.append(1)

        val2 = (values[0] - 1) / 2
        if val2 in values:
            sizes[values.index(val2)] += 1
        else:
            values.append(val2)
            sizes.append(1)

        sizes[0] -= 1
        if sizes[0] == 0:
            values.pop(0)
            sizes.pop(0)

    f_out.write("Case #" + str(t) + ": " + str(values[0] / 2) + " " + str((values[0] - 1) / 2) + "\n")
    #print "Case #" + str(t) + ":", values[0] / 2, (values[0] - 1) / 2


f_in.close()
f_out.close()