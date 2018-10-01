# a quaternion is represented as:
#['+'/'-'  ,  '1'/'i'/'j'/'k']

#axb=c
#x=(a^-1)c(b^-1)
def evaluate(ind1, ind2): #including indexes
    if(ind1 == 0):
        return begin_val[ind2]
    if(ind2 == (len(begin_val) - 1)):
        return end_val[ind1]
    
    a = begin_val[ind1-1]
    b = end_val[ind2+1]
    c = all_val
    t = multiply(getInverse(a), c)
    return multiply(t, getInverse(b))
    
def getInverse(q):
    if(q[EL] == '1'):
        return q[:]
    ans = [0,0]
    ans[EL] = q[EL]
    if(q[SIGN] == '+'):
        ans[SIGN] = '-'
    else:
        ans[SIGN] = '+'
    return ans

def multiply(q1,q2):
    minuses = 0
    if(q1[SIGN] == '-'):
        minuses += 1
    if(q2[SIGN] == '-'):
        minuses += 1
    tmp = multiplyElements(q1[EL],q2[EL])
    if(tmp[SIGN] == '-'):
        minuses += 1
    
    ans = ['','']
    if(minuses % 2 == 0):
        ans[SIGN] = '+'
    else:
        ans[SIGN] = '-'
    ans[EL] = tmp[EL]
    return ans
    
def multiplyElements(el1, el2):
    ind1 = elementToIndex(el1);
    ind2 = elementToIndex(el2)
    return (multiplication_table[ind1][ind2])[:]
    
def elementToIndex(el):
    if(el == '1'):
        return 0
    if(el == 'i'):
        return 1
    if(el == 'j'):
        return 2
    if(el == 'k'):
        return 3
    return -1
        
def main():
    global begin_val
    global end_val
    global all_val
    input1 = open('input1.txt', 'r')
    output1 = open('output1.txt', 'w')

    T = int(input1.readline())      #number of test cases
    
    for casenum in xrange(1, T + 1):
        line = input1.readline().strip().split(' ')
        explen = int(line[0])
        mult_cof = int(line[1])
        expression = input1.readline().strip()
        expression = expression * mult_cof
        explen = len(expression)
        
        begin_val = [0] * explen
        begin_val[0] = ['+', expression[0]]
        for a in xrange(1, explen):
            begin_val[a] = multiply(begin_val[a-1] , ['+',expression[a]])
        end_val = [0] * explen
        end_val[explen-1] = ['+', expression[explen-1]]
        for b in xrange(explen-2,-1,-1):
            end_val[b] = multiply(['+',expression[b]] , end_val[b+1])
        all_val = (begin_val[explen-1])[:]
        
        ans = 'NO'
        br = False
        for a in xrange(0, explen-2):
            if(begin_val[a] == ['+', 'i']):
                for b in xrange(a+1, explen-1):
                    if(end_val[b+1] == ['+','k']):
                        if(evaluate(a+1,b) == ['+', 'j']):
                            ans = 'YES'
                            br = True
                    if(br):
                        break
            if(br):
                break
        
        outstr = 'Case #' + str(casenum) + ': '
        outstr += ans
        outstr += '\n'
        output1.write(outstr)
        print casenum
        
    input1.close()
    output1.close()

SIGN = 0
EL = 1
multiplication_table = [[['+','1'] , ['+','i'] , ['+','j'] , ['+','k']],\
                        [['+','i'] , ['-','1'] , ['+','k'] , ['-','j']],\
                        [['+','j'] , ['-','k'] , ['-','1'] , ['+','i']],\
                        [['+','k'] , ['+','j'] , ['-','i'] , ['-','1']]]
begin_val = 0   #begin_val[a] = evaluate(0,a)
end_val = 0     #begin_val[b] = evaluate(b,explen-1) 
all_val = 0     #all_val = evalueate(0,explen-1)

main()