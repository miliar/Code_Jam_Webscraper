#Open input
case_file = open('inb.txt')
total_cases = int(case_file.readline())
case_string = case_file.read()
lines= case_string.splitlines()
previous = 0
lineN = 0




for case in xrange(1,total_cases +1):
    A,B,K = [int(number) for number in lines[case-1].split()]
    options = 0
    for a in xrange(A):
        for b in xrange(B):
            if a&b < K:
                options += 1
    print "Case #{0}: {1}".format(case,options)