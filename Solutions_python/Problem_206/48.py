input_file = 'A-large.in'
output_file = 'A.out'

with open(input_file) as f:
    with open(output_file, 'w') as out:
        cases = f.readline()
        cases = int(cases)
        for i in xrange(1, cases+1):
            d, horses = map(int, f.readline().split())
            max_time = 0
            for j in range(horses):
                k, speed = map(int, f.readline().split())
                max_time = max(max_time, 1.*(d-k)/speed)
                print max_time

            res = 1.*d/max_time
            print 'Case #{i}: {z}'.format(z=res, i=i)
            out.write('Case #{i}: {z}\n'.format(z=res, i=i))