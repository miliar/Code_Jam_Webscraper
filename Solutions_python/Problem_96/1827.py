
def calc(text):
    list = text.split()
    n = int(list[0])
    print "n = ", n, "\n"
    s = int(list[1])
    print "s = ", s, "\n"
    p = int(list[2])
    print "p = ", p, "\n"
    t = []
    for i in range(0, n):
        t.append(int(list[i+3]))
        print "t[",i,"] = ", t[i]
    ok = 0
    # main shit
    for j in range(0, n):
        if (t[j] == 0 and p == 0):
            ok = ok+ 1
        elif (t[j] >= p):
            num = t[j] / 3
            z = t[j] % 3
            
            r = p - num
            
            if (r > 0):
                if (r == 2):
                    if ((s != 0) and (z != 0)):
                        s = s - 1
                        ok = ok + 1
                elif (r == 1):
                    if (z == 0): 
                        if (s != 0):
                            s = s - 1
                            ok = ok + 1
                    else:
                        ok = ok + 1
            else:
                ok = ok + 1
    print "fline ", ok
    return ok

def main():
    f = open('/home/nikita/input.txt', 'r')
    f2 = open('/home/nikita/out.txt', 'w')
    num = int(f.readline())
    for i in range(1, num+1):
        text = f.readline()
        out = calc(text)
        f2.write("Case #" +str(i) + ": " + str(out) + "\n")
        #f2.write(text + " : " + str(out) + "\n")
        
main()