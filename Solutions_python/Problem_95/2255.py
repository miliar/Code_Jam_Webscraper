inp = {'ejp mysljylc kd kxveddknmc re jsicpdrysi' : 'our language is impossible to understand' ,
       'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd': 'there are twenty six factorial possibilities'  ,
       'de kr kd eoya kw aej tysr re ujdr lkgc jv' : 'so it is okay if you want to just give up' ,
       }
L = []

d={'y' : 'a' , 
   'e' : 'o'   ,
   'q':'z'   ,
   }

for g,e in inp.items():
    g=g.replace(' ','')
    e = e.replace(' ','')
    l = len(g)
    z = zip(g,e)
    L.extend(z)

for g,e in L:
    if g in d and d[g] != e:
        raise str((g,e,d))
    else:
        d[g] = e
d['z'] = 'q'
d[' ']=' '
ii = open('input')
oo = open('output','w')
lines = ii.readlines()
assert int(lines[0].strip())==len(lines)-1
import operator
out = []
for i,line in enumerate(lines[1:]):
    ss = 'Case #%d: %s'%(1+i,reduce(operator.add,map(lambda x:d[x],line.strip()))) 
    out.append( ss )
    print ss
print >> oo, '\n'.join(out)