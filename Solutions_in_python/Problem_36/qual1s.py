#!/usr/bin/env python
import types;

s = "elcomew elcome to code jam"
welcome = 'welcome to code jam';
a=list();

def nextletter(letter, welcomepos, stringpos,str):
    length=len(str);
    a=list();
    for i, c in enumerate(str):
            if(c==letter and i < (length-(18-welcomepos)) and i >= stringpos):
                    a.insert(0,i);
    return a;

def brains(a, welcomepos,str):
    b=list();
    for i, position in enumerate(a):
        if(type(position) is types.ListType):
            realpos = position[len(position)-1];
        else:
            realpos = position
        next = nextletter(welcome[welcomepos], welcomepos, realpos,str)
        #print 'next, a, welcomepos, str', next, a, welcomepos, str
        if(type(a[0]) is types.ListType):
            for newstr in next:
                entry = a[i][:];
                entry.append(newstr);
                b.append(entry);
            
        else:
            for newstr in next:
                entry = [ a[i], newstr];
                b.append(entry);
    return b;
#a = nextletter('w',0,0,s);
#print a;
#
#
#for i in range(1,19):
#    a = brains(a, i);
#
#print len(a);

# read input
f = open('C-small-attempt0.in', 'r')
w = open('output.out', 'w')
num = int(f.readline().strip())
print 'num', num;
for i in range(1,num+1):
    w.write('Case #'+str(i)+': ')
    s = f.readline().strip()
    a = nextletter('w',0,0,s);
    
    for j in range(1,19):
        #print a, j, s, welcome[j]
        a = brains(a, j,s);
    mystr = "%04d" % len(a)
    w.write(mystr[(len(mystr)-4):]);
    w.write('\n');
f.close()