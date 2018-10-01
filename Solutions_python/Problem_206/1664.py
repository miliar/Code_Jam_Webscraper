import sys

# def single_horse_problem(D, K, S):
#     return (D*S)/float(D - K)

def single_horse_problem(D, h, extra_t):
    K, S = h
    return D / ((float(D - K)/S) + extra_t)

def time_horse_merge(h1, h2):
    return (h2[0] - h1[0]) / float(h1[1] - h2[1])

def horse(D, KS):
    KS_speed = sorted(KS, key=lambda horse: horse[1], reverse=True)

    bottleneck_horse = KS_speed.pop()
    total_t = 0.0
    while KS_speed:
        next_bottleneck_horse = KS_speed.pop()
        if next_bottleneck_horse[0] < bottleneck_horse[0]:
            t = time_horse_merge(next_bottleneck_horse, bottleneck_horse)
            merge_k = t*next_bottleneck_horse[1] + next_bottleneck_horse[0]
            if merge_k < D:
                bottleneck_horse = (merge_k, bottleneck_horse[1])
                total_t += t
            else:
                bottleneck_horse = next_bottleneck_horse
                total_t = 0.0
    return single_horse_problem(D, bottleneck_horse, total_t)




if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = input_file.split('.')[0] + '_output.txt'
    with open(input_file, 'rb') as f:
        with open(output_file, 'wb') as o:
            T = int(f.readline().rstrip())
            case_num = 1
            while T > 0:
                DN = f.readline().rstrip().split(' ')
                D, N = int(DN[0]), int(DN[1])
                KS = []
                for i in xrange(N):
                    KiSi = f.readline().rstrip().split(' ')
                    KS.append((int(KiSi[0]), int(KiSi[1])))
                answer = horse(D, KS)
                o.write("Case #" + str(case_num) + ": " + str(answer) + '\n')
                T -= 1
                case_num += 1
    # D = 300
    # KS = [(120, 60), (60, 90)]
    # print horse(D, KS)

