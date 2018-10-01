import sys, re, copy

p = sys.stdin
rowcount = 0
tot_cases = None
cases = []
trigger = None
rows = 0
for row in p:
    if rowcount==0:
        tot_cases = row
    else:
        if rows==0:
            trigger=True
        if trigger==True:
            trigger=False
            rows, cols = [int(item) for item in row.split()]
            og_r = rows
            
#            print rows
            prob = []
            continue
        if rows>0:
            rows-=1
            prob.append(row)
        if rows==0:
            cases.append([(og_r,cols),prob])
            prob = []
    rowcount+=1
answers = []

red = ['/','\\','\\','/']
for case in cases:
    rows,cols = [int(item) for item in case[0]]
    c_grid = [list(item.strip()) for item in case[1]]
    test_grid = copy.deepcopy(c_grid)
    for i in range(rows):
        for g in range(cols):
            test_grid[i][g]=False
    for i in range(rows):
        for j in range(cols):
            if test_grid[i][j]==False:
                try_set = [(i,j),(i,j+1), (i+1,j), (i+1,j+1)]
                trig= True
                for coord in try_set:
                    if coord[0]<rows and coord[1]<cols:
                        if c_grid[coord[0]][coord[1]]=='#':
                            pass
                        else:
                            trig=False
                    else:
                        trig=False
                if trig==True:
                    count = 0
                    for coord in try_set:
                        test_grid[coord[0]][coord[1]]=red[count]
                        count+=1
    didFail = False
    for i in range(rows):
        for g in range(cols):
            if test_grid[i][g]==False and c_grid[i][g]=='#':
                test_grid[i][g]='.'
                didFail= True
            elif test_grid[i][g]==False:
                test_grid[i][g]='.'

    if didFail:
        answers.append('Failed')
    else:
        answers.append(test_grid)
#    print test_grid
        #for row in test_grid:
        #print ''.join(row)
case = 1
for answer in answers:
    st = 'Case #%d:' %case
    sys.stdout.write(st+'\n')
    if answer=='Failed':
            sys.stdout.write('Impossible \n')
    else:
        for row in answer:
            sys.stdout.write(''.join(row)+'\n')


    case+=1
"""

case = 1
for answer in answers:
    st = 'Case #%d: '%case+str(answer)
    sys.stdout.write(st+'\n')
    case+=1
"""        








