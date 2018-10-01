
from sys import argv



if __name__ == '__main__':
    input = open(argv[1])
    max_cases = int(input.readline().strip())

    for case in xrange(max_cases):

        R, k, N = (int(x.strip()) for x in input.readline().strip().split(' '))
        groups = [int(x) for x in input.readline().strip().split(' ')[0:N]]

        euros = 0
        for time in xrange(R):
            ppl = 0
            line = len(groups)
            while True:
                if line == 0 or ppl + groups[0] > k:
                    euros += ppl
                    break
                else:
                    line -= 1
                    newppl = groups.pop(0)
                    ppl += newppl
                    groups.append(newppl)
        
        print "Case #%s: %s" % ((case + 1), euros)


