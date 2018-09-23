from itertools import islice
f_in = open('B-small-attempt1.in','r')
f_out = open('B-small-attempt1.out','w')
t = f_in.readline()
i = 1
for N in islice(f_in,0,100):
    N = N.strip()
    if len(N) == 1:
        f_out.write("Case #" + str(i) + ": "+ N + '\n')
        i += 1
    elif len(N) == 0:
        pass
    else:    
        while (N != ''.join(sorted(N))):
            N = str(int(N) - 1)
        f_out.write("Case #" + str(i) + ": "+ N + '\n')
        i += 1
f_in.close()
f_out.close()
    
    
