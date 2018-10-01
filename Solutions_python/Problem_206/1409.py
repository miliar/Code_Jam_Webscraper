def cruise(d,arr):

    mi = None
    for k,s in arr:
        ti = (d-k)/s
        if mi == None:
            mi = ti
        elif ti > mi:
            mi = ti

    return d/mi


if __name__ == '__main__':

    arr = []
    case = 0
    i,ii,tc = 0,0,0
    h = 0
    p = None

    inp = open('A-large.in.txt',"r")
    out = open('A-large.out.txt',"w")

    for line in inp:
        line = line.strip()
        if len(line) == 0: continue
        if i == 0:
            tc = line
        else:
            if ii == 0:
                [d,n] = map(int,line.split())
                ii = n
            else:
                [k,s] = map(int,line.split())
                arr.append([k,s])
                ii -= 1
                if ii == 0:
                    h += 1
                    s = "Case #"+str(h)+": "+str(cruise(d,arr))
                    out.write(s+"\n")
                    arr = []

        i += 1
