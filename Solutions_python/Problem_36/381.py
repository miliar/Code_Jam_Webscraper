import sys

f = file(sys.argv[1], "r")
out = file(sys.argv[1][:-2] + "out","w")

def read_int_line():
    return int(f.readline().strip())

def read_word():
    return f.readline().strip()        

text = "welcome to code jam"
L = len(text)

def print_matrix(m):
    print "\n".join(["Matching: " + ", ".join([str(e) for e in line]) for line in m])

def solve(line):
    M = len(line)
    if M < L:
        return 0
    matrix = []
    for i in xrange(L):
        matrix.append([])
        for j in xrange(M+1):
            matrix[i].append(0)
    #print_matrix(matrix)
    
    for matching in xrange(0,L): 
        for begin in xrange(M - L + 1):
            subtext = text[matching]
            subline = line[begin+matching]
            if subline == subtext:
                if matching > 0:
                    if matrix[matching - 1][begin + 1] > 0:
                        matrix[matching][begin + 1] = matrix[matching][begin] + matrix[matching - 1][begin + 1]
                else:
                     matrix[matching][begin + 1] = matrix[matching][begin] + 1
                #print_matrix(matrix) 
            else:
                matrix[matching][begin + 1] = matrix[matching][begin]
        for begin2 in xrange(M - L + 1, M):
            matrix[matching][begin2 + 1] = matrix[matching][begin2]
        #print_matrix(matrix)      
    count = matrix[L-1][M]  
    return count
N = read_int_line()
for test_case in xrange(1,N+1):
    count = 0
    line = read_word()
    count = solve(line)

    count = count % 10000
    counts = str(count)
    if count < 1000:
        counts = "0" + counts
    if count < 100:
        counts = "0" + counts
    if count < 10:
        counts = "0" + counts
    r = "Case #%s: %s" % (test_case, counts)
    print r
    out.write(r + "\n")
