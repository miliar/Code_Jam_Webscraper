file_prefix = 'A-large'

with open(file_prefix + '.in', 'r') as f_in:
    t = int(f_in.readline())
    with open(file_prefix + '.out', 'w') as f_out: 
        for i in xrange(t):
            x = f_in.readline().strip().split(' ')
            n, result, b_pre, o_pre, b_pos, o_pos = int(x.pop(0)), 0, 0, 0, 1, 1
            for j in xrange(n):
                u, v = x.pop(0), int(x.pop(0))
                if u == 'B':
                    m = max([abs(v - b_pos) - b_pre, 0]) + 1
                    b_pre, b_pos, o_pre = 0, v, o_pre + m
                else:
                    m = max([abs(v - o_pos) - o_pre, 0]) + 1
                    o_pre, o_pos, b_pre = 0, v, b_pre + m
                result += m
            f_out.write('Case #%s: %s\n' % (i + 1, result))