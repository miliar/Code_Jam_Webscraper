
import time
import sys
import itertools
import math

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = input("Enter filename: ")

#quiet = False
quiet = True

with open(filename,'r') as f:
    with open(filename+'.out','w') as o:
        startTime = time.clock()
        # read the first line
        T = int(f.readline())
        # read all the cases
        for caseNumber in range(1,T+1):
            # read the case
            S,K = f.readline().split(' ')
            K = int(K)
            L = len(S)
            print("Case #{}: L = {}, K = {}".format(caseNumber,L,K))
            if quiet == False:
                print(S)
            # check for total impossibility
            j = S.count('-')
        
                
            #print('Step 0: {}'.format(j))

            # create an iterator of all the valid moves
            nLast = max([0,math.ceil((L-K)/2)])
            
            NumberOfFlips = 0
            # Alternate between left and right
            for n in range(nLast+1):
                yl = n      # leftmost one to flip
                yr = L-n-1  # rightmost one to flip
                if quiet == False:
                    print('L{} R{}'.format(yl,yr))
                # Check left and right in each pair
                if S[yl] == '-':
                    # flip this and to the right
                    # Do the flip
                    s = ''
                    z = ''
                    for x in range(yl,yl+K):
                        if S[x] == '-':
                            s = s + '+'
                            z = z + '*'
                        else:
                            s = s + '-'
                            z = z + '~'
                    S = S[:yl] + s + S[yl+K:]
                    if quiet == False:
                        print(S[:yl] + z + S[yl+K:])
                    NumberOfFlips = NumberOfFlips + 1

                # Check if we flip on the right side
                if S[yr] == '-':
                    # flip this and to the right
                    # Do the flip
                    s = ''
                    z = ''
                    for x in range(yr,yr-K,-1):
                        if S[x] == '-':
                            s = '+' + s
                            z = '*' + z
                        else:
                            s = '-' + s
                            z = '~' + z
                    S = S[:yr-K+1] + s + S[yr+1:]
                    if quiet == False:
                        print(S[:yr-K+1] + z + S[yr+1:])
                    NumberOfFlips = NumberOfFlips + 1
            # It should be done now...
            # If not, then it's impossible
            j = S.count('-')
            if j == 0:
                i = NumberOfFlips
                print('Solved in {} flips.'.format(i))
            else:
                print('NOT SOLVED: {} pancakes remaining.'.format(j))
                i = 'IMPOSSIBLE'

                
            # Print the output file
            o.write('Case #{}: {}\n'.format(caseNumber,i))
            print('Case #{}: {}'.format(caseNumber,i))
            print('--------------------------')

            
        print('Finished in {} seconds.'.format(time.clock()-startTime))
