d={}
d['a']='y'
d['b']='h'
d['c']='e'
d['d']='s'
d['e']='o'
d['f']='c'
d['g']='v'
d['h']='x'
d['i']='d'
d['j']='u'
d['k']='i'
d['l']='g'
d['m']='l'
d['n']='b'
d['o']='k'
d['p']='r'
d['q']='z'
d['r']='t'
d['s']='n'
d['t']='w'
d['u']='j'
d['v']='p'
d['w']='f'
d['x']='m'
d['y']='a'
d['z']='q'

text=open('C:\\Users\\Anshul\\Downloads\\A-small-attempt1.in','r')
N=int(text.readline())
for j in range(N+1):
    line=text.readline()
    line1=''
    for i in range(len(line)):
        if line[i]!=' ' and line[i] in d:
            line1+=d[line[i]]
        elif line[i]==' ':
            line1+=' '
    f=open('C:\\Users\\Anshul\\Downloads\\out4.txt','a')
    f.write('Case #'+str(j+1)+': '+line1+'\n')
