def converter(line):
    convert=dict(y='a',n='b',f='c',i='d',c='e',w='f',l='g',b='h',k='i',u='j',o='k',m='l',x='m',s='n',e='o',v='p',z='q',p='r',d='s',r='t',j='u',g='v',t='w',h='x',a='y',q='z')

    lineout=''
    for char in line:
        if ((char != ' ')and(char != '\n')):
            char=convert[char]
        lineout=lineout+char
    return lineout
file=raw_input('Pls enter name of input file')
f=open(file,'r')
data=[]
for line in f:
    data.append(str(line))
print data
fout=open('output.txt','w')
number=int(data[0])
for c in range(0,number):
    fout.write('Case #')
    fout.write(str(c+1))
    fout.write(': ')
    ans=converter(data[c+1])
    fout.write(ans)
    print ans
fout.close()
