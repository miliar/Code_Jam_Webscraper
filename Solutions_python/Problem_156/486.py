import math
INPUT = "B-small-attempt6.in"
OUTPUT = "B-small-attempt6.out"

def solve(data):
    m = max(data)
    min_sol = m
    if m <= 3:
        return m
    tmp_data = [i-1 for i in data]
    tmp_sol = 1+solve(tmp_data)
    if (tmp_sol < min_sol):
        min_sol = tmp_sol
    root = math.sqrt(m)
    n = root - (root % 1)
    n = int(n) + 1
    for i in range(2,n):
        tmp_data = [j for j in data]
        tmp_data.remove(m)
        m1 = m / i
        r = m % i
        s = m
        while (s > 0):
            if (r>0):
                r-=1
                x = m1+1
            else:
                x = m1
            tmp_data.append(x)
            s-=x
        tmp_sol = i-1+solve(tmp_data)
        if (tmp_sol < min_sol):
            min_sol = tmp_sol
    return min_sol

if __name__=="__main__":
    f_in = open(INPUT)
    f_out = open(OUTPUT,"w")
    lines = f_in.readlines()
    output = []
    cases = int(lines[0].strip())
    for i in range(cases):
        D = int(lines[2*i+1].strip())
        P = [int(j) for j in lines[2*i+2].strip().split(" ")]
        output += "Case #%d: %d\n" % (i+1,solve(P))
        
    f_out.writelines(output)
    f_out.close()
    f_in.close()
    print 'done.'
