

if True:
    input = file('A-large.in').read().split('\n')
    N = int(input[0])
    
    index = 0
    for i in range(N):
        index += 1
        S = int(input[index])
        engines = input[index+1:index+1+S]
        Q = int(input[index+1+S])
        queries = input[index+1+S+1:index+1+S+1+Q]
        index = index+1+S+1+Q-1
        
        searched, switches = 0, 0
        while searched < len(queries):
            try:
                searched += max(map(lambda e: queries[searched:].index(e), engines))
            except ValueError, e:
                break
            switches += 1
        
        output = 'Case #%d: %d' % (i+1, switches)
        file('A-large.out','a').write(output + '\n')
        print output
        
        
