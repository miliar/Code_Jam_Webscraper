import sys

in_name = 'B-small-attempt0.in'
in_name = 'B-large.in'
out_name = 'b_out.txt'
fin = open(in_name, 'r')
fout = open(out_name, 'w')

n = fin.readline()
n = int(n.split('\n')[0])
res = []

for i, line in enumerate(fin):
    value = 0
    line = line.split()
    N, S, p = int(line[0]), int(line[1]), int(line[2])
    points = []
    for j in range(3, N + 3):
        points.append(int(line[j]))
    points.sort()
    min_total_s = max(p*3 -4, p)
    min_total_normal = max(p*3 - 2, p)
    
    # print N, S, p
    # print min_total_s, min_total_normal
    # print points
    
    for point in points:
        if S > 0:
            if point >= min_total_s:
                value += 1
                S -= 1
        else:
            if point >= min_total_normal:
                value += 1
                
    #print "Case #%d: %s" % (i+1, value)
    res.append("Case #%d: %s\n" % (i+1, value))
    
fout.writelines(res)
fout.close()
fin.close()