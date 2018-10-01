# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 23:15:26 2014

@author: Pam
"""
output_f = open('output.txt', 'a')
with open('A-small-attempt0.in', 'r') as f:
    num_cases = int(f.readline())
    f.seek(0)
    for n in range(num_cases):
        case_num = str(n+1)
        case_determiner = 0
        for num, row in enumerate(f):
            if num == n*10+1:
                first_row_ind = num+int(row)
            elif num == n*10+6:
                second_row_ind = num+int(row)
        f.seek(0)
        for num, row in enumerate(f):
            if num == first_row_ind:
                first_row = row.split()
            elif num == second_row_ind:
                second_row = row.split()
        for item in second_row:
            if item in first_row:
                case_determiner+=1
                same = item
        if case_determiner == 0:
            notice = 'Volunteer cheated!'
        elif case_determiner == 1:
            notice = same
        elif case_determiner > 1:
            notice = 'Bad magician!'
        print 'Case #'+case_num+': '+notice
        line_out ='Case #'+case_num+': '+notice+'\n'
        output_f.write(line_out)
        f.seek(0)
            
       
output_f.close()
