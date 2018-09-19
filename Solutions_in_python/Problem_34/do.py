from alien import *
import sys

fd = open(sys.argv[1],'r')
head = fd.readline()
head = head.split()
L = int(head[0])
D = int(head[1])
N = int(head[2])

D_list = []

for i in range(D):
    D_list.append(fd.readline().strip())

fd2 = open(sys.argv[2], 'w')
for i in range(N):
    fd2.write('Case #%d: %d\n' % (i+1, decipher(L, D_list, fd.readline().strip())))

fd.close()
fd2.close()
