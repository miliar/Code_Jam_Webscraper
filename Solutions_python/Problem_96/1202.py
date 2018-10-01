import sys
import math    

def init():
    print 'begin'
    out = open(sys.argv[2], 'w')
    f = open(sys.argv[1], 'r')
    test_cases = []
    ans = []
    f.readline()
    for line in f:
        tmp = line.split(" ")
	test_cases.append((tmp[0],tmp[1],tmp[2], tmp[3:]))

    for case in test_cases:
        goal = int(case[2])
        surprise = int(case[1])
        res = 0
        for g in case[3]:
          tot = float(g)
          floor = math.floor(float(g) / 3 )
          if goal > float(g):
            continue
          v1 = goal
          v2  = math.ceil((tot - goal) / 2.0 )
          v3  = math.floor((tot - goal) / 2.0 )


          if v1 - v3 <= 1:
            res += 1
          elif v1 - v3 <= 2 and surprise > 0:
            res += 1
            surprise -= 1
        ans.append(res)
          
    ind = 1
    for a in ans:
        out.write("Case #" + str(ind) +": ")
        out.write(str(a))
        out.write("\n")
        ind +=1

init()
