prob = "b"
size = "small"

f = open('{0}-{1}.in'.format(prob, size))
o = open('{0}-{1}.out'.format(prob, size), 'w+')
n = int(f.readline());

for t in range(n):
    line = f.readline().split()
    
    maps = {}
    opposed = []
    invoked = ""
    to_invoke = line[~0]
    
    map_count = int(line[0])
    opposed_count = int(line[map_count+1])
    to_invoke_count = int(line[~1])
    
    for m in line[1:map_count+1]:
        base = m[0:2]
        non_base = m[2:3]
        maps[base] = non_base
        maps[base[::-1]] = non_base
        
        
    if opposed_count > 0:    
        for z in range(opposed_count):
            opposed.append(line[map_count+2:map_count+2+opposed_count][0])
        
    for i in to_invoke:
        invoked += i

        if len(invoked) >= 2:
            last_two = invoked[-2:]
            if last_two in maps:
                invoked = invoked[0:-2] + maps[last_two]
                continue
            
            for p in opposed:
                found = 0
                for l in p:
                    if invoked.find(l) >= 0: found = found + 1
                if ( found == 2 ): invoked = ""
                break
    solution =  ', '.join(list(invoked))
    o.write("Case #{0}: {1}\n".format(t+1, '['+solution+']'))