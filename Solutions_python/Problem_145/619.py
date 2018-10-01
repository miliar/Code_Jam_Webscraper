import math
import fileinput

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

indata = [line for line in fileinput.input()]
cases = int(indata[0])
line_no = 1

for case_no in range(1, cases+1):
    (a, b) = indata[case_no].split('/')
    (a, b) = (int(a), int(b))
    g = gcd(a, b)
    (a, b) = (a/g, b/g)
    result = 1
    while(True):
        if a*2 < b:
            a = a * 2
            result = result + 1
        else:
            break

    if math.log(b, 2) == int(math.log(b, 2)):
        print 'Case #%d: %d' % (case_no, result)
    else:
        print 'Case #%d: impossible' % (case_no)