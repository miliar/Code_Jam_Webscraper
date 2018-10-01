
import math
def find_distances(n, k):
    while k != 0:
        biggest_interval = max(n)
        n.remove(biggest_interval)
        lesser_half = int(math.floor((biggest_interval - 1) / 2.0))
        bigger_half = int(math.ceil((biggest_interval- 1) / 2.0))
        k = k - 1
        n = n +[lesser_half, bigger_half]
        #import pdb;pdb.set_trace()
    return bigger_half, lesser_half
    
import sys
def main():
    input_file = open(sys.argv[1],'r')
    points = int(input_file.readline().strip())
    for i in range(points):
        n, k = input_file.readline().split()
        n = int(n)
        k = int(k)
        a, b = find_distances([n],k)
        #import pdb;pdb.set_trace()
        print 'Case #%d:' % (i+1,), a, b
        

if __name__ == '__main__':
    main()