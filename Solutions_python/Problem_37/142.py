'''
Created on Sep 12, 2009

@author: fu4ny
'''
nonHappyBase = [[] for _ in xrange(11)]
happyBase = [[] for _ in xrange(11)]
def tobase(b,n,result=''):
        if n == 0: 
            if result == '':
                return '0'
            return result
        else: 
            return tobase(b,n/b,str(n%b)+result)
        
def happyCheck( number, base=10):
    past = []
    while True:
        number = tobase(base,number)
        total = sum( [int(i)**2 for i in str(number)])
        if total == 1 or total in happyBase[base]:
            happyBase[base].append(past)
            return bool(1)
        if total in past:
            nonHappyBase[base].append(past)
            return bool(0)
        number = total
        past.append(total)
    
ifs = open('input.txt','r')
ofs= open('output.txt','w')
numberOfTest = ifs.readline()[:-1]
for test in range(int(numberOfTest)):
    print 'Running Test %i' % test
    bases = ifs.readline()
    if bases[-1] == '\n': bases = bases[:-1]
    bases = bases.split(' ')
    i = 2
    while True:
        for k in bases:
            if not happyCheck(i,int(k)): break
        else: 
            ofs.write('Case #%i: %i\n' % (test,i))
            break
        i += 1
ofs.close()


    
