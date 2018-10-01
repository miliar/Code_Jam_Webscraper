fin = open("A-large.in","rt")

n = int( fin.readline().rstrip('\n') )

fout = open("OUTPUT","wt")
for x in range(n):
    tup = fin.readline().rstrip('\n').split(" ")
    s = list(tup[0])
    nn = int(tup[1])
    ct = 0
    for y in range(len(s)):
        if s[y] == '-':
            if y<=len(s)-nn:
                ct += 1
                for z in range(nn):
                    if s[y+z] == '-': s[y+z] = '+'
                    else: s[y+z] = '-'
            else:
                ct = -1
                break
    st = "Case #" +str(x+1)+": "
    if ct == -1: st += "IMPOSSIBLE"
    else: st += str(ct)
    print st
    fout.write(st+'\n')
fout.close()
