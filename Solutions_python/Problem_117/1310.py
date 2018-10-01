with open('input.in') as f:
    
    outfile = open('output.out','w')
    
    cases = int(f.readline())
    for case in range(1,cases+1):
        n,m = [int(a) for a in f.readline().split(' ')]
        lawn = []
        for row in range(n):
            lawn.append([int(a) for a in f.readline().split(' ')])
        print lawn
        
        max_in_row = []
        max_in_col = []
        for row in lawn:
            max_in_row.append(max(row))
        for k in range(m):
            max_in_col.append(max([row[k] for row in lawn]))
        
        print max_in_row
        print max_in_col
        
        canit = True
        for row in range(n):
            for col in range(m):
                if lawn[row][col] < min(max_in_col[col],max_in_row[row]):
                    print row
                    print col
                    canit = False
                    break
            if not canit:
                break
        
        if canit:
            outfile.write('Case #%d: YES\n' % case)
        else:
            outfile.write('Case #%d: NO\n' % case)
    outfile.close()