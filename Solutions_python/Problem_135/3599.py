
# imports
import sys
import os


def Main():
    datafile = os.path.basename(__file__).replace('.py', '.txt')
    resultsfile = os.path.basename(__file__).replace('.py', '_results.txt')

    data = [] 
    with open(datafile) as f:
        data = f.readlines()

    idx = 0
    numtests = int(data[idx].strip())
    idx = idx + 1

    print 'numtests = %d' % numtests

    linespertest = 10

    print '-'*30

    results = []
    for i in range(numtests):
        print '-'*20

        tidx = idx + linespertest * i
        guess1 = int(data[tidx])

        cards1 = []
        cards1.append(data[tidx + 1].split())
        cards1.append(data[tidx + 2].split())
        cards1.append(data[tidx + 3].split())
        cards1.append(data[tidx + 4].split())
        
        guess2 = int(data[tidx + 5])
        cards2 = []
        cards2.append(data[tidx + 6].split())
        cards2.append(data[tidx + 7].split())
        cards2.append(data[tidx + 8].split())
        cards2.append(data[tidx + 9].split())
        

        print guess1
        print '\n'.join([', '.join(x) for x in cards1])

        print '-'*10
        print guess2
        print '\n'.join([', '.join(x) for x in cards2])

        print '-'*10

        # -- rows are 1 - 4 (not 0-3) 
        guess1row = set(cards1[guess1 - 1])
        guess2row = set(cards2[guess2 - 1])

        res = guess1row.intersection(guess2row)
        print res
        #print guess1row 
        #print guess2row 
        
        if len(res) == 1:
            # -- again, not 0 based indices
            results.append('Case #%d: %d' % (i+1, int(res.pop())))
        elif len(res) == 0:
            results.append('Case #%d: Volunteer cheated!' % (i+1))
        elif len(res) > 0:
            results.append('Case #%d: Bad magician!' % (i+1))
            
    print '-'*30


    with open(resultsfile, 'w') as f:
        f.write('\n'.join(results))

    return 0

if __name__ == "__main__":
    sys.exit(Main())
