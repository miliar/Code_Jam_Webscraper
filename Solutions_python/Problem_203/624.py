with open('input.txt', 'rU') as f:
    with open('output.txt', 'w') as fout:
        lines = f.readlines()

        i = 1
        q = 0
        while i < len(lines):

            q += 1
            fout.write('Case #')
            fout.write(str(q))
            fout.write(': \n')

            line = lines[i].rstrip()
            r = int(line.split()[0])
            c = int(line.split()[1])

            complete = [False] * r
            lastLine = ''

            for j in xrange(i + 1, i + r + 1):
                lines[j] = lines[j].rstrip()
                curr = ''
                newLine = ''
                for k, c in enumerate(lines[j]):
                    if k == 0 and c != '?':
                        curr = c
                        newLine += c
                    elif k > 0 and curr != '' and c == '?':
                        newLine += curr
                    elif k > 0 and c != '?':
                        if curr == '':
                            newLine = c * (k+1)
                        else:
                            newLine += c
                        curr = c
                if newLine != '':
                    w = j - i - 1
                    while w >= 0 and (not complete[w]):
                        lines[w + i + 1] = newLine
                        complete[w] = True
                        w -= 1
                    lastLine = newLine
                    
            if complete[-1] == False:
                w = r - 1
                while w >= 0 and (not complete[w]):
                    lines[w + i + 1] = lastLine
                    complete[w] = True
                    w -= 1
            
            
            for j in xrange(i+1, i+r+1):
                fout.write(lines[j] + '\n')
            i += r + 1
