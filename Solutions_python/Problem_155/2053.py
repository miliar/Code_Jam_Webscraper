#!/usr/bin/python
def main():
    T = 0
    open("a.out", 'w').close()
    with open("a.in") as f:
        line = f.readline()
        T = int(line)
        for case in range(1, T+1):
            line = f.readline()
            tmp = line.split()
            ret = solve(int(tmp[0]), tmp[1])
            with open("a.out", 'a') as fout:
                fout.write("Case #" + str(case) + ": " + str(ret) + "\n")
                fout.close()
        f.close()

def solve(Smax, seats):
    cur = 0; guests = 0
    for i in range(0, Smax+1):
        if (cur < i):
            guests += (i-cur)
            cur += (i-cur)
        cur += int(seats[i])

    return guests            
    
main()
