import string

from_str = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""

to_str = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""

maping_table = {'y':'a','e':'o','q':'z'}
for i in range(len(from_str)):
    maping_table[from_str[i]] = to_str[i]

missing_k = set(string.lowercase).difference(set(maping_table.keys()))
missing_v = set(string.lowercase).difference(set(maping_table.values()))

maping_table[missing_k.pop()] = missing_v.pop()

#test
#for c in string.lowercase:
#    print c,':',maping_table[c]

f = open('A-small-attempt2.in')
f_out = open('A-small-attempt2.out','w')
num_of_cases = int(f.readline())
for i in range(1,num_of_cases+1):
    s = f.readline()
    result = ''
    for c in s:
        result+=maping_table[c]
    res = 'Case #%d: %s' % (i,result)
    f_out.write(res)
f.close()
f_out.close()
