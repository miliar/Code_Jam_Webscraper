import math
input_file = "B-large.in"


def line(f,_type=str):
    s = [_type(i) for i in f.readline().strip().split()]
    return s


with open(input_file) as fin:
    with open('output.txt','w') as fout:
        T = line(fin,int)[0]
        for case in range(1,T+1):
            D = line(fin,int)[0]
            p = line(fin,int) #list of pancakes
            L = []
            for eats in range(1,max(p)+1):
                n = eats + sum(max(math.ceil(float(i)/eats) - 1, 0) for i in p)
                L.append(int(n))
            print "Case #%d: %d" % (case, min(L))
            fout.write("Case #%d: %d\n" % (case, min(L)))
            
