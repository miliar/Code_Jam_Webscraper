import sys

def cookie(c, f, x):
    # print "c=%f, x=%f, f=%f"%(c, x, f)
    t = 0.0
    cps = 2.0
    time_to_farm = c/cps
    while True:
        t += time_to_farm
        #buy farm:
        time_to_x_1 = x/(cps+f)
        #do not buy:
        time_to_x_2 = (x-c)/cps
        if time_to_x_1 < time_to_x_2:
            cps += f
            time_to_farm = c/cps
        else:
            t += time_to_x_2
            break
    return t
    
def procfile(fname):
    retval = []
    with open(fname, "r") as f:
        n = int(f.readline())
        for i in range(n):
            retval.append([float(s) for s in f.readline().split()])
    return retval
        
def main():
    fname = sys.argv[1]
    result = procfile(fname)
    cnt = 1
    for (c, f, x) in result:
        print "Case #%d: %.07f"%( cnt, cookie(c, f, x))
        cnt = cnt+1
    
if __name__ == "__main__":
    main()