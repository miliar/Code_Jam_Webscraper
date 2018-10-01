import os, sys

print(os.getcwd())
f = open('in.txt','r')
o = open ('out.txt','w')
p = sys.__stdout__

cases = f.readline().strip()

case = 0
for l in f:
    case += 1
    print(l + ' ')
    
    ls = l.split()
    
    num_scores = ls[0]
    num_sup = int(ls[1])
    min_sco = int(ls[2])
    
    num_with_min_score = 0
    
    for score in ls[3:]:
        score = int(score)
        if min_sco == 0:
            num_with_min_score += 1
            continue
        if min_sco == 1:
            if score > 0:
                num_with_min_score += 1
            continue
            
        if score >= (min_sco * 3) - 2:
            num_with_min_score += 1
        elif score >= (min_sco * 3) - 4 and num_sup > 0:
            num_with_min_score += 1
            num_sup -= 1




    o.write('Case #' + str(case) + ': ' + str(num_with_min_score) + '\n')



o.close()
f.close()


