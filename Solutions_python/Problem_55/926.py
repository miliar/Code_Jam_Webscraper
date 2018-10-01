#! /usr/bin/env python
import os
import sys

def main():
	if len(sys.argv) != 2 or sys.argv[1].startswith('-'):
		print 'Usage: %s <directory>' % sys.argv[0]
		sys.exit(-1)


filename = sys.argv[1]
print filename

input = open(filename, 'r')
output = open('out.txt', 'w')

L = input.readline()
num = int(L)
print num

for i in range(num):
    print "num:%s" % i
    L1 = input.readline()
    itemList = L1.split()
    tmp = [ int(item) for item in itemList ]
    R = tmp[0]
    k = tmp[1]
    N = tmp[2]
#     if R < 1: R = 1
#     if R > 1000: R = 1000
#     if k < 1: k = 1
#     if k > 100: k = 100
#     if N < 1: N = 1
#     if N > 10: N = 10
    print R, k, N
            
    L2 = input.readline()
    peopleList = L2.split()
    people = [ int(item) for item in peopleList ]
    print people
    print len(people)

    cnt = 0
    total = 0
    for j in range(R):
        seat = 0
        queue = 0
        while seat <= k:
            print 'k-seat %d' % (k-seat)
            if (people[cnt%N] <= (k-seat)) and (queue < N):
                seat += people[cnt%N]
                cnt += 1
                queue += 1
            else:
                break
            print 'cnt/N: %d' % (cnt%N)
        print 'seat:%d' % seat
        total += seat
    
    print 'total Euro:%d' % total

    output.write('Case #%d: %d \n' % (i+1, total))
    #print 'Case #%d: %d' % (i+1, total)

input.close()
output.close()

if __name__=='__main__':
	main()
