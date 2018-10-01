# Imports
from operator import itemgetter
import math

# Constants
DEBUG = True

f_name = 'A-large.in'#'test.in'#'A-small-attempt4.in'#
f2_name = 'A.out'

def keyfunc(x):
    return 2*x['R']*x['H']*math.pi

with open(f_name) as f:
    with open(f2_name,'w') as f2:
        T = int(f.readline()) # Discard first line
        for i in range(1, T+1):
            result = ''
            # Do the processing of each line
            N, K = f.readline().split()
            N = int(N)
            K = int(K)
            pancakes = []
            #area = 0
            for j in range(N):
                R, H = f.readline().split()
                R = int(R)
                H = int(H)
                pancakes.append({'R': R, 'H': H})
            
            bestarea = 0
            oldnewlist = sorted(pancakes, key=keyfunc, reverse=True)
            for j in range(N-K+1):
                newlist = oldnewlist[:K-1]
                newlist.append(oldnewlist[K-1+j])
                #newlist = sorted(oldnewlist[j:], key=keyfunc, reverse=True)[:K]
                first = max(newlist, key=itemgetter('R'))
                area = math.pow(first['R'], 2)*math.pi
                for k in range(K):
                    area += 2*newlist[k]['R']*newlist[k]['H']*math.pi
                bestarea = max(bestarea, area)
            #print(newlist)
            result = '{0:.9f}'.format(bestarea)
            # Print this line
            print("Case #{}: {}".format(i, result), file=f2)

if DEBUG:
    with open(f2_name) as f2:
        for line in f2:
            print(line, end='')