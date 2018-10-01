# the main function that outputs to a file
def b(filename):
    fd = open(filename, 'rU')
    cases = int(fd.readline())
    out = []
    #read the file
    for i in range(cases):
        rows, cols = [int(j) for j in fd.readline().split(' ')]
        pattern = []
        for j in range(rows):
            pattern.append(tuple([int(n) for n in fd.readline().split(' ')]))
        result = evaluate(tuple(pattern),rows, cols)
        out.append('Case #{0}: {1}'.format(i+1,result))
    fd.close()
    

    #write to the output file
    fd = open('output.txt', 'w')
    for s in out:
        fd.write(s+'\n')
    fd.close()

# the subfunction that does most of the computation
def evaluate(pattern, rows, cols):
    """Evalutes if pattern is possible or not

    evaluate(tuple<tuple<int>>, int, int) -> str

    """
    transpose = tuple(zip(*pattern))
    for i in range(rows):
        for j in range(cols):
            row_set = set([n for n in pattern[i] if n > pattern[i][j]])
            col_set = set([n for n in transpose[j] if n > pattern[i][j]])
            if row_set & col_set:
                return 'NO'
    return 'YES'
