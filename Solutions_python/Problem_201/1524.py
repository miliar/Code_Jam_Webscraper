def problem3():
    f = open("C-small-1-attempt0.in", "r")
    f2 = open("C-small-1-attempt0.out", "w")
    line = f.readline()
    for i in range(1, int(line.strip())+1):
        start, time = f.readline().strip().split()
        start = int(start)
        time = int(time)
        l = []
        for index in range(0, time):
            if start <2:
                left = 0
                right = 0
                break
            left = int(start/2)
            right = start - left - 1
            l.append(left)
            l.append(right)
            start = max(l)
            l.remove(start)
        f2.write("Case #" + str(i) + ": " + str(max(left,right)) + " " +
                 str(min(left,right)) + "\n")    
    f.close()
    f2.close()


problem3()
