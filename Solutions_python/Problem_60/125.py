import sys

def check_possible(times,T):
    min_times = sorted(times)
    for i in range(K):
        if min_times[i][0] > T:
            return False
    return True

f = open(sys.argv[1],'r')

cases = int(f.readline())

for i in range(1,cases+1):
   N,K,B,T = [int(x) for x in f.readline().strip().split()]
#   print "Need %d chickens in %d seconds (Barn at %d)" % (K,T,B)
   locations = [int(x) for x in f.readline().strip().split()]
   speeds = [int(x) for x in f.readline().strip().split()]
   chickens = zip(locations,speeds)
   chickens.sort(reverse=True)
   min_times = [((B-x[0])*1.0/x[1],x[0],x[1]) for x in chickens]
   if check_possible(min_times,T):
       swaps = -(K*(K-1)/2)
       found = 0
       for x,chick in enumerate(min_times):
           if chick[0] <= T and found < K:
               swaps+=x
               found+=1

       print "Case #%d: %d" % (i,swaps)

   else:
       print "Case #%d: IMPOSSIBLE" % i
