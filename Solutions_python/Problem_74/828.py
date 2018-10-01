import sys

def findNextMove(robot, seq):
    i = 0
    while i < len(seq) and seq[i] != robot:
        i+=2
        
    if i >= len(seq):
        return None
    
    return int(seq[i+1])

def makeMove(robot, seq, (curPos, targetPos)):
    if targetPos == None:
        return seq, (curPos, targetPos)
        
    if curPos > targetPos:
        return seq, (curPos-1, targetPos)
    elif curPos < targetPos:
        return seq, (curPos+1, targetPos)
    elif seq[0] == robot and int(seq[1]) == curPos:
        seq = seq[2:]
        return seq, (curPos, findNextMove(robot, seq))
    else:
        return seq, (curPos, targetPos)

def main():
    cases = int(raw_input())
    
    for c in xrange(1, cases+1):
        seq = raw_input().split()[1:]
        orange = (1, findNextMove('O', seq))
        blue = ([1, findNextMove('B', seq)])
        
        counter = 0
        while len(seq) > 0:
            newseq1, orange = makeMove('O', seq, orange)            
            newseq2, blue = makeMove('B', seq, blue)
            
            if len(newseq1) != len(seq):
                seq = newseq1
            elif len(newseq2) != len(seq):
                seq = newseq2
#                
#            print seq
#            print orange
#            print blue
            counter += 1
        
        result = counter
        print "Case #%d: %d"%(c, result)
        #print >> sys.stderr, "Case #%d: %d"%(c, result)
        
if __name__ == '__main__':
    main()
