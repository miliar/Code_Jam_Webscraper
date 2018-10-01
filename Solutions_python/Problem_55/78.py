# the function to calculate the GCD
def gcd(a,b):
	"""gcd(a,b) returns the greatest common divisor of the integers a and b."""
	if a == 0:
		return b
	return abs(gcd(b % a, a))

# the function to calculate the LCM
def lcm(num1, num2):
    result = num1*num2/gcd(num1,num2)
    return result

input = open('3.in', 'r')
output = open('3.out', 'w')
n = int(input.readline())

from collections import deque

for i in range(1,n+1):
    (R,k,N) = [int(x) for x in input.readline().split(' ')]
    # R = number of rounds
    # k = limit of coaster
    # (group size, round, euros)
    gi = [int(x) for x in input.readline().split(' ')]
    if sum(gi) <= k:
        output.write("Case #%d: %d\n" % (i, R*sum(gi)))
        continue
    gi = deque([(int(x), 0, 0) for x in gi])
    euros = 0
    round = 0
    while round < R:
        boarded = 0
        (g, r, e) = gi[0]
        while g+boarded <= k:
            boarded = g + boarded
            gi.append(gi.popleft())
            (g, r, e) = gi[0]
        euros += boarded
        round += 1
        (g,r,e) = gi[0]
        if r>0:
            l = round - r
            delta = euros - e
            cycles = (R - round) / l
            round = round + cycles * l
            euros = euros + cycles * delta
        else:
            gi[0] = (g,round,euros)
    output.write("Case #%d: %d\n" % (i, euros))
        
        
        

#   if 0 == (K+1) % pow(2,N):
#       print "%d %d ON" % (N,K)
#       output.write('Case #' + str(i) + ": ON\n")
#   else:
#       print "%d %d OFF" % (N,K)
#       output.write('Case #' + str(i) + ": OFF\n")

