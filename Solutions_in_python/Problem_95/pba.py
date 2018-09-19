from string import maketrans 
inp="ynficwlbkuomxsevzpdrjgthaq"
out="abcdefghijklmnopqrstuvwxyz"
trans = maketrans(inp, out)
a=open('C:/Users/chetan/Desktop/A-small-attempt2.in','r')
b=a.readline()
d=a.readlines()
i=0
while i<int(b):
    c=d[i]
    c=c.translate(trans)
    d[i]='Case #%s: %s' % (i+1,c)
    i=i+1
a.close()
a=open('C:/Users/chetan/Desktop/out.txt','w')
a.writelines(d)
a.close()

