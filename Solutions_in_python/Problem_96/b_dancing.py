import pprint

out_fd = open('b_large.out', 'w')

with open('b_large.in') as in_fd:
    n = int(in_fd.readline())
    for i, line in enumerate(in_fd):
        out_fd.write('Case #{0}: '.format(i + 1))
        fields = map(int, line.split())
        N, S, p = fields[0], fields[1], fields[2]
        scores = fields[3:]

        print N, S, p

        num_passed = 0
        for score in scores:
            if score >= p + 2 * max(0, p - 1):
                # exceeds p without being surprising
                num_passed += 1
                print score, "exceeds p without being surprising"
                continue
            if score >= p + 2 * max(0, p - 2):
                print 'trying to use surprising'
                if S > 0: # exceeds p, being surprising
                    num_passed += 1
                    S -= 1
                    print score, "exceeds p while being surprising"
        out_fd.write('{0}\n'.format(num_passed))
out_fd.close()
