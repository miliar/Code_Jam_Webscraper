
import sys
i1=sys.stdin.readline()
i=int(i1);
redak=''
m=0
while m<i:
    redak+= sys.stdin.readline()
    m+=1
a=[]
anjj=redak.split('\n')
for elem in anjj:
    if elem<>'': a.append(elem)
rijecnik={}

##########
rijecnik['a']='y'
rijecnik['b']='h'
rijecnik['c']='e'
rijecnik['d']='s'
rijecnik['e']='o'
#f
rijecnik['g']='v'
rijecnik['h']='x'
rijecnik['i']='d'
rijecnik['j']='u'
rijecnik['k']='i'
rijecnik['l']='g'
rijecnik['m']='l'
rijecnik['n']='b'
rijecnik['o']='k'
rijecnik['p']='r'
#q
rijecnik['r']='t'
rijecnik['s']='n'
rijecnik['t']='w'
rijecnik['u']='j'
rijecnik['v']='p'
rijecnik['w']='f'
rijecnik['x']='m'
rijecnik['y']='a'
#z

rijecnik['q']='z'
rijecnik['z']='q'
rijecnik['f']='c'

rjesenje=''
mm=1;
for elem in a:
    rjesenje+='Case #'+str(mm)+': '
    mm+=1
    for ch in elem:
        if ch.isalpha():
            rjesenje+=rijecnik[ch]
        else:
            rjesenje+=ch
    rjesenje+='\n'
    

print rjesenje


