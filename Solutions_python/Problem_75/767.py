file = open('B-large.in', 'r')

lines = [l.strip() for l in file]
num_cases = int(lines.pop(0))

for idx, line in enumerate(lines[:num_cases], 1):
    tokens = line.split(' ')
    c = int(tokens.pop(0))
    
    combinations = {}
    
    for i in range(0,c):
        trio = tokens.pop(0)
        combinations[trio[:2]] = trio[2:]
    
    d = int(tokens.pop(0))
    
    eliminations = {}
    
    for i in range(0,d):
        duo = tokens.pop(0)
        try:
            eliminations[duo[0]].add(duo[1])
        except KeyError, e:
            eliminations[duo[0]] = set(duo[1])
        try:
            eliminations[duo[1]].add(duo[0])
        except KeyError, e:
            eliminations[duo[1]] = set(duo[0])
    
    invoke_list = tokens.pop(1)
    
    working = ""
    for k in invoke_list:
        tail = working[-1:] + k
        
        if combinations.has_key(tail):
            working = working[:-1] + combinations[tail]
        elif combinations.has_key(tail[::-1]):
            working = working[:-1] + combinations[tail[::-1]]
        elif eliminations.has_key(k) and set(working).intersection(eliminations[k]):
            working = ""
        else:
            working += k
    
    print "Case #%s: [%s]" % (idx, ', '.join(working))