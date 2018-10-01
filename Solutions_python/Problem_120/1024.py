'''
Created on 2013. 4. 13.

@author: purepleya
'''
import math

def solve():
    f = open('A-small-attempt0.in', 'r') 
    out_file = open('A-small-attempt0.out', 'w')
    
    lines = f.readlines()
    line_index = 0
    case_count = int(lines[0])
    
    for case_index in range(0, case_count):
        
        line_index += 1
        r = int(lines[line_index].replace('\n', '').split(' ')[0])
        t = int(lines[line_index].replace('\n', '').split(' ')[1])
        
        circle_cnt = check(r, t)
        
        out_file.write('Case #%d: %d\n' % (case_index + 1, circle_cnt)) 
        
    f.close()
    out_file.close()
    
    print 'finish'
    

def check(r, t):
    sumPaint = 0
    circleCnt = 0
#    circleCnt = int(math.ceil(pow(2, 0.5)))
    
    while True:
        sumPaint += (2 * r)  + (4 * (circleCnt + 1)) - 3
        if sumPaint > t:
            break
        circleCnt += 1
    return circleCnt


if __name__ == '__main__':
#    print int(math.ceil(pow(2, 0.5)))
    solve()