from decimal import *
getcontext().prec = 7

def cal(c, f, x, n):
    time = 0.0
    rate = 2.0
    while (n > 0):
        time += c/rate
        rate += f
        n -= 1
    time += x/rate
    return time
    
    
def calculate(c, f, x):
    min_time = -1
    cur_cost = 0
    i = 0
    while 1:
        r = cal(c,f,x,i)
        if (min_time < 0):
            min_time = r
        elif(r < min_time):
            min_time = r
        i += 1
        cur_cost = c*i
        if (cur_cost > x):
            break
        
    return min_time


def main():
    inpfile = open("B-small-attempt0.in", 'r')
    outfile = open('outfile', 'w')
    casenum = int(inpfile.readline().strip())
    for case in range(1, casenum + 1):
        line = inpfile.readline().strip()
        linelst = line.split()
        c = float(linelst[0])
        f = float(linelst[1])
        x = float(linelst[2])
        
        result = calculate(c, f, x)
        result = "{0:.7f}".format(result)
        
        result = "Case #" + str(case) + ": " + result+"\n"
        print result
        outfile.write(result)
    inpfile.close()
    outfile.close()




if __name__ == "__main__":
    
    main()
    

    
    