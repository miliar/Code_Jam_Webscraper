
import string


def compute(line):
    answer = 0
    words = string.split(line,' ')
    values = []
    for w in words : 
        values.append(int(w))

    n = values[0]
    s = values[1]
    mini = values[2]
    rest = values[3:]
    flag = 0 
    supr_flag = 0
    l = [ -2 , -1, 0 ,1 , 2 ]
    for r in rest : 
        ans = []
        summ = r
        lower =  (summ - 4)/3
        upper =  (summ + 4)/3
        #print "L , U " , lower , upper
        if lower < 0 : 
            lower = 0
        if upper < 0 : 
            upper = 0
        for  i in range(lower,upper+1):
            for p in l : 
                for q in l : 
                    if (( 3 * i ) + p + q == summ) and (i >= 0) and (i + p >= 0) and (i + q >= 0) and ( abs(p-q) <= 2) :
                        if abs(p) == 2 or abs(q) == 2 or (abs(p-q) == 2) : 
                            if  s  and (not supr_flag) and (not flag): 
                                ans = [ i , i + p ,i + q]   
                                if max(ans) >= mini : 
                                    s = s - 1 
                                    supr_flag = 1
                        else : 
                            ans = [ i , i + p ,i + q]                           
                            if max(ans) >= mini  : 
                                flag = 1 
                                if supr_flag : 
                                    s = s + 1
                                    supr_flag = 0
        if not flag : 
            if supr_flag : 
                answer = answer + 1
        else : 
            answer = answer + 1
        flag = 0
        supr_flag = 0
    return answer

l = raw_input()

t = int(l) 
testcases = 1;
while t : 
    line = raw_input()
    print "Case #" + str(testcases) + ":", compute(line)
    t = t - 1
    testcases = testcases + 1
