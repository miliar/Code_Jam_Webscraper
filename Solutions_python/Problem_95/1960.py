mapping = 'ynficwlbkuomxsevzpdrjgthaq '
letters = 'abcdefghijklmnopqrstuvwxyz '
with open("output1.txt",'w') as out:
    with open("input1.txt") as f:
        t = int(f.readline().strip())
        for x in range(1,t+1):
            line = f.readline().strip()
            out.write('Case #%d: ' % x)
            for c in line:
                out.write(letters[mapping.index(c)])
            out.write("\n")
