f = open('b.in')
cases = int(f.readline())
case = 1
while (case <= cases):
    task = f.readline()
    task = task.strip()
    c = int(task.split(' ',1)[0])
    task = task.split(' ', 1)[1]

    c_ = 0
    combines = {}
    while c_ < c:
        combine = task.split(' ', 1)[0]
        task = task.split(' ', 1)[1]
        combines[combine[0:2]]= combine[2]
        combines[combine[1::-1]]= combine[2]
        
        c_ += 1
    
    d = int(task.split(' ',1)[0])
    task = task.split(' ', 1)[1]
    
    d_ = 0
    opposites = []
    while (d_<d):
        opposite = task.split(' ', 1)[0]
        task = task.split(' ', 1)[1]
        opposites.append(opposite)
        opposites.append(opposite[::-1])
        d_ += 1
        
    n = int(task.split(' ',1)[0])
    task = task.split(' ', 1)[1]
    
    solution = []
    previous_element = task[0]  
    solution.append(previous_element)
    i = 1  
    while i<n:        
        current_element = task[i]
        if previous_element+current_element in combines.keys():
            solution.pop()
            solution.append(combines[previous_element+current_element])
            previous_element = combines[previous_element+current_element]            
        else:
            solution.append(current_element)
            previous_element = current_element

        clear_solution = False
        
        for k in range(len(solution)-1):
            for m in range(k+1, len(solution)):
                if solution[k]+solution[m] in opposites:
                    clear_solution = True
        
        if clear_solution:
            solution = []
            i += 1
            if i>=n:
                break
            previous_element = task[i]
            solution.append(previous_element)
                    
        i += 1
        
    s = ''
    for el in solution:
        s += el+', '
    len_s = len(s)
    if len_s>0:
        s = s[0:len_s-2]
    print "Case #"+str(case)+": ["+s+"]"
    case += 1 