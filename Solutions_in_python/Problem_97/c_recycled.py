import pprint

out_fd = open('c.out', 'w')

with open('c.in') as in_fd:
    n = int(in_fd.readline())
    for i, line in enumerate(in_fd):
        out_fd.write('Case #{0}: '.format(i + 1))
        A, B = map(int, line.split())
        N = len(str(A))
        n_recycled = 0

        for num in range(A, B + 1):
            recycled = {}
            num_str = str(num)
            for i in range(1, N):
                num2 = int(num_str[i:] + num_str[:i])
                if num2 > num and num2 <= B and num2 not in recycled:
                    recycled[num2] = 1
                    n_recycled += 1

        out_fd.write('{0}\n'.format(n_recycled))
out_fd.close()
