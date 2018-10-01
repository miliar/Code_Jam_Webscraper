import re

raw = open('A-large.in').read().split('\n')

a1 = map(lambda s:s.strip(), raw)

if len(a1) == 0:
    exit();
    
dictcount = int(a1[0].split(' ')[1])
dict = '@' + '@@'.join(a1[1:dictcount+1]) + '@'

countx = 0

b = open('xxx1.out','w')

for tmp in filter(lambda s:len(s), a1[dictcount+1:len(a1)]):
    countx+=1
    b.write( 'Case #' + countx.__str__() + ': ' + len(re.findall('@' + tmp.replace('(','[').replace(')',']') + '@',dict)).__str__() + '\n')
    

    

