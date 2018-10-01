#class LoopExit(BaseException):
#   pass

def bin_add(a, b):
    longer = max(len(a), len(b))
    if len(a) < longer:
        a = '0'*(longer-len(a)) + a
    if len(b) < longer:
        b = '0'*(longer-len(b)) + b
    result = ''
    
    for da, db in zip(a,b):
        if da == db:
            result += '0'
        else:
            result += '1'
    return result

#print bin_add('1001', '11')

def process(inputs):
    inputs = [ int(x) for x in inputs]
    result = ''
    for input in inputs:
        result = bin_add(result, bin(input)[2:])
    for d in result:
        if d == '1':
            return 'NO'
    return str(sum(inputs) - min(inputs))


fin = open('C-large.in', 'r')
fout = open('C-large.out', 'w')
t = int(fin.readline().rstrip())
for i in range(1, t+1):
    line = int(fin.readline().rstrip())
    result = process(fin.readline().rstrip().split(' '))
    fout.write('Case #%d: %s\n' % (i, result))
    
fin.close()
fout.close()

