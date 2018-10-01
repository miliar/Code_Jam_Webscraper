import math

if __name__ == '__main__':
    input = open('./source/A-large-0.in', 'r')
    output = open('./source/A-large-0.out', 'w')

    n = int(input.readline().strip())
    for i in range(n):
        total = 0
        o_prev = 1
        o_require = o_pass = 0
        b_prev = 1
        b_require = b_pass = 0
        seq = input.readline().strip().split()
        step = int(seq[0])
        for j in range(0, step):
            obj = seq[j*2 + 1]
            pos = int(seq[j*2 + 2])
            if obj == 'O':
                o_require = math.fabs(pos - o_prev) + 1
                if o_require <= o_pass:
                    b_pass += 1
                    total += 1
                else:
                    b_pass += o_require - o_pass
                    total += o_require - o_pass
                o_prev = pos
                o_pass = 0
            else:
                b_require = math.fabs(pos - b_prev) + 1
                if b_require <= b_pass:
                    o_pass += 1
                    total += 1
                else:
                    o_pass += b_require - b_pass
                    total += b_require - b_pass
                b_prev = pos
                b_pass = 0
        print >>output, "Case #%d: %d" % (i+1, total)
            
            
