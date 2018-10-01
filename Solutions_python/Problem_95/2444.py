

code = {'y':'a', 'e':'o', 'q':'z', 'z':'q'}

inp = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
       "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
       "de kr kd eoya kw aej tysr re ujdr lkgc jv"]

out = ["our language is impossible to understand",
       "there are twenty six factorial possibilities",
       "so it is okay if you want to just give up"]

for i, line in enumerate(inp):
    for j, c in enumerate(line):
        cur = code.get(c) 
        if cur:
            if cur != out[i][j]:
                print "ERROR: Had '%c'->'%c' = '%c'" % (c, cur, out[i][j])
                quit()
        else:
            code[c] = out[i][j]
       

with open(r"C:\Users\User\Downloads\A-small-attempt0.in", "r") as f:
    f.readline()

    i = 1
    for line in f:
        s = ""
        for c in line.strip():
            s += code[c]
        
        print 'Case #%d: %s' % (i, s)
        i += 1

    
