"""Code written using Python 2.7.1, http://www.python.org/"""

def calc(case):

    (N, S, p) = [int(e) for e in case.split()[0:3]]
    print 'Surprises:', S, 'score:', p
    googlers = [int(e) for e in case.split()[3:]]
    print googlers
    result = 0
    for g in googlers:
        if (g/3.0 > p-1 and (p-1 > 0 or g/3.0 > 0)) or p == 0:
            print '+1 for', g
            result += 1
        elif g/3.0 > p-2 and S > 0 and (p-2 > 0 or g/3.0 > 0):
            print '+1 for', g, '*'
            result += 1
            S -= 1

    print result
    return result




f = open('B-small.in', 'r')
lines = f.readlines()   
f.close()
c = lines[0].split()[0]
#print c     
cases = [r.strip() for r in lines[1:]]
#print cases  

of = open('output_b_small.txt', 'w')

for idx, case in enumerate(cases):
    print '***********',idx+1,'*************'
    of.write('Case #%(idx)i: %(i)i\n' % {'idx': idx + 1, 'i': calc(case)})                          

of.close()
