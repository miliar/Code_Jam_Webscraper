#class LoopExit(BaseException):
#   pass

def process(inputs):
    inputs = [ int(x) for x in inputs ]
    moves = 0
    for i, value in enumerate(inputs):
        if i+1 != value:
            moves += 1
    
    return float(moves)


fin = open('D-large.in', 'r')
fout = open('D-large.out', 'w')
t = int(fin.readline().rstrip())
for i in range(1, t+1):
    line = int(fin.readline().rstrip())
    result = process(fin.readline().rstrip().split(' '))
    fout.write('Case #%d: %s\n' % (i, result))
    
fin.close()
fout.close()

