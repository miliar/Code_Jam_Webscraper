__author__ = 'jlinenthal'

def good(b):
    return len(b) == len(list(filter(lambda x: x == '+', b)))

#filename = "A-small-attempt0"
#filename = "ATest"
filename = "A-large"

infile = filename+ ".in"
outfile = filename+ ".out"

f_in = open(infile, 'r')
f_out = open(outfile, 'w')

t = int(f_in.readline().strip())

for aaa in range(0,t):
    line = f_in.readline().strip()
    nOrig = list(map(lambda x: 0 if x == '-' else 1, line.split(" ")[0]))
    k = int(line.split(" ")[1])

    n = list(nOrig)
    curFlips = 0;
    print(str(n))
    for i in range(0,len(n)):
        if n[i] == 1:
            continue
        if i + k > len(n):
            curFlips = -1
            break
        curFlips += 1
       # print(str(n[i:(i+k)]))
        n[i:(i+k)] = list( map(lambda x: 1 if x == 0 else 0, n[i:(i+k)]) )
      #  print(str(n[i:(i+k)]))
      #  print(str(n))

    nz = list(nOrig[::-1])
    curFlips2 = 0;
   # print(str(nz))
    for i in range(0,len(n)):
        if nz[i] == 1:
            continue
        if i + k > len(n):
            curFlips2 = -1
            break
        curFlips2 += 1
       # print(str(n[i:(i+k)]))
        nz[i:(i+k)] = list( map(lambda x: 1 if x == 0 else 0, nz[i:(i+k)]) )
      #  print(str(n[i:(i+k)]))
      #  print(str(n))

    res = min(curFlips, curFlips2)
    if curFlips == -1 and curFlips2 == -1:
        f_out.write("Case #{0}: {1}\n".format(aaa+1, "IMPOSSIBLE"))
    elif curFlips == -1:
        f_out.write("Case #{0}: {1}\n".format(aaa+1, curFlips2))
    elif curFlips2 == -1:
        f_out.write("Case #{0}: {1}\n".format(aaa+1, curFlips))
    else:
        f_out.write("Case #{0}: {1}\n".format(aaa+1, res))
    print(i,curFlips, curFlips2)



#line = f_in.readline().strip()
#k = int(line.split()[0])
#c = int(line.split()[1])

