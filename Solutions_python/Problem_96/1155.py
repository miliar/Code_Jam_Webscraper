def dance_score(l, i):
    count = 0
    flag = 0
    n = int(l[0])
    surp = int(l[1])
    p = int(l[2])
    inp = l[3:]
    inp = map(int, inp)
    inp.sort()
    x = 0

    for j in inp:
        temp =  int(j) - p
        temp /= 2
        if flag == 1 and j >= x:
            count += 1
        elif temp >= p - 1 and temp >= 0:
            count += 1
            flag = 1
            x = j
        elif temp >= p - 2 and temp >= 0 and surp >= 1:
            count += 1
            surp -= 1
     
    fout = open("output.txt", "a")
    fout.write("Case #" + str(i) + ": ")
    fout.write(str(count))
    fout.write("\n")
    fout.close()
        

fin = open("file.txt", "r")

n = int(fin.readline())
for i in range(n):
    line = fin.readline()
    l = line.split()
    dance_score(l, i+1)


