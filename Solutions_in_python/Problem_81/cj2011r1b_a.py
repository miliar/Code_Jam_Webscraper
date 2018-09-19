#!/usr/bin/python
import sys


if len(sys.argv) == 3:
    lines = open(sys.argv[1], 'r').readlines()
    fw = open(sys.argv[2], 'w')
else:
    sys.exit('Usage: %s in_filename out_filename' % sys.argv[0])


"""
lines = ['2'
,'3'
,'.10'
,'0.1'
,'10.'
,'4'
,'.11.'
,'0.00'
,'01.1'
,'.10.']
"""

numofcases = int(lines[0])
cursor = 1
for i in range(0, numofcases):
    
    N = int(lines[cursor])
    cursor += 1
    
    sch = []
    for j in range(0, N):
        sch.append(list(lines[cursor].replace('\n', '')))
        cursor += 1
    
    
    wp = []
    for j in range(0, N):
        cnt = 0.0
        sum = 0.0
        for k in range(0, len(sch[j])):
            if sch[j][k] != '.':
                cnt += 1.0
                if sch[j][k] == '1': sum += 1.0
        if cnt>0: sum /= cnt
        wp.append(sum)
    
    owp = []
    for j in range(0, N):
        cnt = 0.0
        sum = 0.0
        for k in range(0, N):
            if sch[j][k] != '.':
                tmp_cnt = 0.0
                tmp_sum = 0.0
                for l in range(0, N):
                    if sch[k][l] != '.' and l != j:
                        tmp_cnt += 1.0
                        if sch[k][l] == '1': tmp_sum += 1.0
                if tmp_cnt>0: tmp_sum /= tmp_cnt   
                cnt += 1.0
                sum += tmp_sum
        if cnt>0: sum /= cnt
        owp.append(sum)
    
    oowp = []
    for j in range(0, N):
        cnt = 0
        sum = 0
        for k in range(0, N):
            if sch[j][k] != '.':
                tmp_cnt = 0.0
                tmp_sum = 0.0
                for l in range(0, N):
                    if sch[k][l] != '.' and l != j:
                        tmp_cnt += 1.0
                        tmp_sum += owp[k]
                if tmp_cnt>0: tmp_sum /= tmp_cnt
                cnt += 1.0
                sum += tmp_sum
        if cnt>0: sum /= cnt
        oowp.append(sum)
    
    print wp, owp, oowp
    
    print 'Case #%d:' % (i+1)
    for j in range(0, N):
        print 0.25*wp[j] + 0.5 * owp[j] + 0.25 * oowp[j]
    
    fw.write('Case #%d:\n' % (i+1))
    for j in range(0, N):
        fw.write('%f\n'%(0.25*wp[j] + 0.5 * owp[j] + 0.25 * oowp[j]))

fw.close()
