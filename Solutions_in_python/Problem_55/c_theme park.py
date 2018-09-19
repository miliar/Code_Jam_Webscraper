#! /usr/bin/env python
# -*- coding: utf_8 -*-

input_name = "C-small-attempt0.in"
output_name = "C-small.out"

T = 0 #число тестов / number of test cases
R = 0 #количество запусков горки / roller coaster run times
k = 0 #вместимость парка в чел. / roller coaster hold people at once
N = 0 #количество групп посетителей / number of groups
g = 0 #размер группы посетителей, чел. / size of a group

i_begin = 0 #
i_end = 0 #

def main():
    print ('---===RUN===---')
    
    input_file = open(input_name, 'r')
    output_file = open(output_name, 'w')
    
    T = int(input_file.readline())
#    print('T =', T)
    for case in range(1, T+1):
#        print('case =', case)
        rkn = input_file.readline().split()
        R = int(rkn[0])
#        print('R =', R)
        k = int(rkn[1])
#        print('k =', k)
        N = int(rkn[2])
#        print('N =', N)
#        print('rkn =', rkn)
        gi = input_file.readline().split()
#        print('gi =', gi)
#        print()
        profit = 0

        i_g = 0
        i_g_p = 0
        for run in range(1, R+1):
#            print('run =', run)
            fullness = int(gi[i_g])
            while fullness < k:
                i_g += 1
                if i_g > len(gi)-1:
                    i_g = 0
                if i_g == i_g_p:
                    i_g -= 1
                    break
                fullness += int(gi[i_g])
            if fullness > k:
                fullness -= int(gi[i_g])
                i_g -= 1
            i_g += 1
            if i_g > len(gi)-1:
                i_g = 0
            i_g_p = i_g
#            print('fullness =', fullness)
            profit += fullness
#        print('profit =', profit)
        output_file.write('Case #' + str(case) + ': ' + str(profit) + '\n')

#        print()
    
    input_file.close()
    output_file.close()
    
    print ('---===STOP===---')

if __name__ == '__main__':
    main()
