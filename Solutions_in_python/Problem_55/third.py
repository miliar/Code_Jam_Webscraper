import sys

fp = open('small.in', 'r')
out = open('output', 'w')
#out = sys.stdout
cases = int(fp.readline())

for case in range(cases):
    parms = [int(x) for x in fp.readline().split()]
    sizes = [int(x) for x in fp.readline().split()]
    
    rides = parms[0]
    cap = parms[1]
    
    group = 0
    result = 0
    for x in range(rides):
        dentro = 0
        jafoi = 0
        primeiro = group
        while dentro + sizes[group] <= cap:
            if jafoi and group == primeiro:
                break
#            print sizes[group],
            dentro += sizes[group]
            result += sizes[group]
            group = (group + 1) % len(sizes)
            jafoi = 1
#        print
    
    out.write('Case #' + str(case + 1) + ': ' + str(result) + '\n')
    case += 1
