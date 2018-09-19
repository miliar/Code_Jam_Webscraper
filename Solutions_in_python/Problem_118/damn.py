from math import sqrt
from math import ceil
f = open("Output.txt", "w")

def pal(x):
   return all(x[a]==x[-a-1] for a in xrange(len(x)>>1))

i = 0
for e in open("Input.txt", "r"):
    if i != 0:
        list = e.split(' ')
        
        start = int(list[0])
        s_sqrt = int(ceil(sqrt(start)))
        end = int(list[1][:-1])
        e_sqrt = int(sqrt(end))
        f_and_s = 0
        for nr in xrange(s_sqrt, e_sqrt+1):
            numar = nr**2
            if pal(str(numar)) and pal(str(nr)):
                f_and_s += 1
        ans = "Case #" + str(i) + ": " + str(f_and_s) + "\n"
        f.write(ans)
    i += 1
f.close()
