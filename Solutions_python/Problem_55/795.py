

#author:Rafael Pinheiro
import sys

input_file = open(sys.argv[1])  

#number of runs
r = None
#roller coaster maximum capability
k = None
#num of test cases
t = None

groups = []

lines = input_file.readlines()
line = 1
t = int(lines[0])
for tc in range(1, t+1):
    r, k, n = lines[line].split(' ')
    r = int(r)
    n = int(n)#num of groups
    k = int(k)
    groups = [int(x) for x in lines[line+1].split(' ')]
    line += 2
    euros = 0    
    for ride in range(r):
        sits_left = k
        groups_left = n
        #print groups[0], sits_left
        while groups_left > 0 and groups[0] <= sits_left:
            g = groups.pop(0)
            sits_left -= g
            groups_left -= 1
            groups.append(g)
        euros += k - sits_left
            
    print('Case #%d: %d' % (tc, euros))
