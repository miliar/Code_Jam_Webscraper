inputfile = r'A-large.in'
outputfile = r'A-large.out'

#input
def input_data():
    import os
    os.chdir(r'C:\codejam')
    FILENAME = inputfile 
    f = open(FILENAME)
    lines = f.readlines()
    f.close()
    return lines

#output
def output_data(ans):    
    fout = open(outputfile, 'wt')
    print(ans, file = fout)
    fout.close()

from operator import itemgetter
import math

if __name__ == '__main__':
    lines = input_data()

    #calc
    T = int(lines.pop(0)[:-1])
    ans = ''
    for i_t in range(T):
        pi = math.pi
        N, K = map(int, lines.pop(0)[:-1].split())
        l = []
        for i_n in range(N):
            R, H = map(int, lines.pop(0)[:-1].split())
            SH = 2 * pi * R * H
            S = pi * R ** 2 + 2 * pi * R * H
            SR = pi * R ** 2
            l.append([R, H, SH, S, SR])
        l = sorted(l, key = itemgetter(2), reverse = True)
        l_best_h = l[:K]
        l_best_h_r = sorted(l_best_h, key = itemgetter(0),reverse = True)
        minR = l_best_h_r[0][0]
        l_rest = l[K:]
        l_rest = sorted(l_rest, key = itemgetter(3),reverse = True)
        cand = [0] * 5
        for pan in l_rest:
            if pan[0] > minR:
                cand = pan
                break
        if l_best_h[-1][2] < cand[3] - l_best_h_r[0][4]:
            l_best_h[-1] = cand
        ansS = 0
        l_ans = sorted(l_best_h, key = itemgetter(0), reverse = True)
        for pan in l_ans[1:]:
            ansS += pan[2]
        ansS += l_ans[0][3]
        ansline = 'Case #' + str(i_t+1) + ': %.7f' % round(ansS, 7) + '\n'
        ans += ansline
    output_data(ans)
