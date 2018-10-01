filename_in = 'in'
filename_out = 'out'

f_in = open(filename_in, 'r')
f_out = open(filename_out, 'w')

T = int(f_in.readline().strip())

for case_num,line in enumerate(f_in):
    splitline = line.strip().split()
    S_max = int(splitline[0])
    S_counts = map(int, splitline[1])

    extras = 0
    total = 0
    for i in range(S_max+1):
        total += S_counts[i]
        if total <= i:
            extras += 1
            total += 1

    f_out.write("Case #{:d}: {:d}\n".format(case_num+1, extras))

f_out.close()
f_in.close()
