import fileinput
import logging
import sys

logging.basicConfig(stream=sys.stderr,level=logging.DEBUG)


nTest = 0
line_no = 0
instances = []

lines =[]

for line in fileinput.input():
    lines.append(line)

i=0
while i < len(lines):
    line = lines[i]
    if i == 0:
        nTest = int(line)
        logging.debug("%d" % nTest)
    else:
        a = line.split()
        #print a
        # print line, i, a
        n = int(a[0])
        m = int(a[1])
        b = []
        for x in xrange(n):
            i = i+1
            b.append(list(lines[i].rstrip()))
        instances.append((n,m,b))
    i = i+1

def empty(line):
    for i in xrange(len(line)):
        # print line[i],i
        if line[i] != '?':
            #print "returning", False
            return False
    #print "returning", True
    return True

def instance(inst):
    n = inst[0]
    m = inst[1]
    board = inst[2]

    logging.debug(board)
    for i in xrange(n):
        if empty(board[i]):
            pass
        else:
            this = board[i]
            prev = 0
            for j in xrange(m):
                if (this[j] != '?'):
                    for k in xrange(prev,j):
                        this[k]=this[j]
                    prev = j+1
            if prev < m:
                for k in xrange(prev,m):
                    this[k] = this[prev-1]
    for i in xrange(n):
        if empty(board[i]):
            #print "empty", empty(board[i])
            inc = 1
            if i== n-1:
                inc = -1
            full_index = i+ inc
            #print inc, full_index, board[full_index]
            while (empty(board[full_index])):
                full_index+=inc
                if (full_index == n):
                    inc = -1
                    full_index +=inc
                   
                   
            for j in xrange(m):
                   board[i][j] = board[full_index][j]

    #print board
    return board
                

out_line_no = 1
for x in instances:
    result = instance(x)
    print "Case #%d:" % out_line_no
    for i in range(len(result)):
        print ''.join(result[i])
    out_line_no+=1


