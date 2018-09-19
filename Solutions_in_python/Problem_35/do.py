from water import *

import sys

fd = open(sys.argv[1], 'r')
fd2 = open(sys.argv[2], 'w')
n = int(fd.readline().strip())
for i in range(n):
    head = fd.readline().strip().split()
    H = int(head[0])
    W = int(head[1])
    lines = []
    for j in range(H):
        lines.append(fd.readline())
    map_array = build_map(lines)
    check_map(map_array, W, H)
    fd2.write('Case #%d:\n' % (i+1))
    draw_map(fd2, map_array)

fd.close()
fd2.close()
