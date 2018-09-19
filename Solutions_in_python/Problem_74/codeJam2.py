import psyco
psyco.full()

def solver(L):
    L = L.split()[1:]
    line = [(L[i], L[i+1]) for i in xrange(0,len(L),2)]
    
    count = 0	
    prev = {"O":1,"B":1}
    time = {"O":0,"B":0}

    for next in line:
        bot, num, otherBot = next[0], int(next[1]), 'O'
        if bot == "O": otherBot = 'B'
        step = abs(prev[bot]-num) + 1
        prev[bot] = num
        time[bot] = max(time[bot] + step, time[otherBot] + 1)
        count = time[bot]
    return count		

f = open("test.out", 'w')
cases = open("test.in", 'r').readlines()[1:]
for i in range(0, len(cases)):
    line = "Case #" + str(i+1) + ": " + str(solver(cases[i]))
    print line
    f.write(line + "\n")
f.close()
