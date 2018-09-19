import math

if __name__ == '__main__':
    #f = open('sample.in')
    #output = open('sample.out', 'w')
    f = open('B-small-attempt1.in')
    output = open('B-small-attempt1.out', 'w')
    test_case = int(f.readline())
    for i in range(test_case):
        line = f.readline()
        line = line.split()
        D = float(line[0])
        N = int(line[1])
        A = int(line[2])
        if N == 2:
            line = f.readline()
            line = line.split()
            s_1 = float(line[1])
            line = f.readline()
            line = line.split()
            t_1 = float(line[0])
            s_2 = float(line[1])
            v_other = (s_2 - s_1) / t_1
            A_L = f.readline()
            A_L = A_L.split()
            s = 'Case #%s: ' %(i+1)
            output.write(s + '\n')
            for acce in A_L:
                acce = float(acce)
                t = (v_other + math.sqrt(v_other*v_other + 2*acce*s_1)) / acce
                d_tra = 0.5 * acce * t * t
                if d_tra >= D:
                    real_t = math.sqrt(2*D / acce)
                else:
                    real_t = t + (D - d_tra) / v_other
                output.write(str(real_t) + '\n')
        else:
            s = 'Case #%s: ' %(i+1)
            output.write(s + '\n')
            f.readline()
            A_L = f.readline()
            A_L = A_L.split()
            for acce in A_L:
                acce = float(acce)
                time = math.sqrt(2*D / acce)
                output.write(str(time) + '\n')
    f.close()
    output.close()

