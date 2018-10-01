import sets
f = open('r1.in','r')
f2 = open('ro.txt','w')
total = f.readline()

for t in range(1, int(total)+1):
    txt = f.readline().split()
    name = txt[0]
    n = int(txt[1])
    set1 = set([])
    for i in range(len(name)-n+1):
        subStr = name[ i : i + n]
        if(('a'  in subStr or 'e'  in subStr or 'i'  in subStr or 'o'  in subStr or 'u' in subStr) == False):
            for j in range(i+1):
                #print '#####'
                #print name[j:i+n]+str(j)+str(i+n)
                set1.add(name[j:i+n]+str(j)+str(i+n))
                for k in range(i+n+1,len(name)+1):
                    #print '????'
                    #print name[j:k]+str(j)+str(k)
                    set1.add(name[j:k]+str(j)+str(k))
    #print set1
    result = 'Case #'+str(t)+': '+ str(len(set1))
    print result
    f2.write(result+'\n')
    steps = 0
f.close()
f2.close()
