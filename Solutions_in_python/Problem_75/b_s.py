# coding:utf-8
import sys



argvs = sys.argv
argc = len(argvs)

#print argvs
#print argc
f = open(argvs[1])
T = f.readline()

for i in range(int(T)):
    comb_rules = []
    oppo_rules = []
    
    line = f.readline()
    tc = line.split(' ')
    C = int(tc[0]) # 変換ルールの個数
    for j in range(C):
        temp = tc[j+1]
        t_l  = [[temp[0], temp[1]], temp[2]]
        comb_rules.append(t_l)
        t_l  = [[temp[1], temp[0]], temp[2]]
        comb_rules.append(t_l)
    D = int(tc[C+1]) # 反発ルールの数
    for j in range(D):
        temp = tc[j + C + 2]
        t_l = [temp[0], temp[1]]
        oppo_rules.append(t_l)
        t_l = [temp[1], temp[0]]
        oppo_rules.append(t_l)
    
    N = tc[C+D+2] # 文字数
    S = tc[C+D+3] # 文字列
    ls = []


    for j in range(int(N)):

        temp = S[j]
        
        for l in comb_rules:
            if l[0][0] == temp and len(ls) > 0 and l[0][1] == ls[len(ls)-1]:
                ls.pop()
                temp = l[1]
        
        chk = 0
        for l in oppo_rules:
            lss = set(ls)
            if l[0] == temp and l[1] in lss:
                ls = []
                chk = 1
                
        if chk == 0:
            ls.append(temp)

    ans_s = str(ls)
    sys.stdout.write("Case #")
    sys.stdout.write(str(i+1))
    sys.stdout.write(": ")
    sys.stdout.write(ans_s.replace("'",""))
    sys.stdout.write("\n")
    
#    print ls

        
f.close
