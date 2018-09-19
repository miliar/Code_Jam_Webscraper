import os

os.chdir(r'D:\ypsun\codejam\2013\Qualification Round\B. Lawnmower')
job = 'B-small-attempt2'

def setter(input=None):
    """ Read input file and return case in order
    
    """
    cases = int(input.readline())
    for case in xrange(cases):
        lawn = []
        total_row, total_col = map(int, input.readline().split())
        for i in xrange(total_row):
            row = map(int, input.readline().split())
            lawn.append(row)
        yield case+1, total_row, total_col, lawn
    
def h_limit(lawn, total_row):
    h = set([])
    for row in lawn:
       h.update(set(row))
    return min(h), max(h)
    
def farmer(lawn, total_row, total_col, h_min, h_max):
    # get check set
    lawn_set = {}
    for i in xrange(total_row):
        index = str('r'+str(i))
        lawn_set[index] = lawn[i]
    for j in xrange(total_col):
        index = str('c'+str(j))
        lawn_set[index] = []
        for i in xrange(total_row):
            lawn_set[index].append(lawn[i][j])
    # plant
    pt_to_plant = set([])
    plant_count = 0
    for index, v in lawn_set.items():
        if set(v) == set([h_min]) and h_min < h_max+1:
            plant_count += 1
            if index[0] == 'r':
                for j in xrange(total_col):
                    pt_to_plant.add((int(index[1]), j))
            elif index[0] == 'c':
                for i in xrange(total_row):
                    pt_to_plant.add((i, int(index[1])))                   
    for i, j in pt_to_plant:
        lawn[i][j] += 1
    # check
    h_set = set([]) 
    for i in xrange(total_row):
        for j in xrange(total_col):
            h_set.add(lawn[i][j])
    if plant_count == 0:
        return 'NO'
    elif h_set == set([h_max]) or h_set == set([h_max+1]):
        return 'YES'
    else:
        return lawn
    
# main
input = open(job + '.in', 'r')
output = open(job + '.out', 'w')

for case, total_row, total_col, lawn in setter(input):  
    while True:
        h_min, h_max = h_limit(lawn, total_row)
        lawn = farmer(lawn, total_row, total_col, h_min, h_max)
        if lawn in ['YES', 'NO']:
            output.write('Case #%(case)s: %(lawn)s\n' % locals())
            # print 'Case #%(case)s: %(lawn)s\n' % locals()
            break
            
input.close()
output.close()
        
