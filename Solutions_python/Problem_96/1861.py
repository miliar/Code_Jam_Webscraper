fin = open("B-small-attempt3.in")
fout = open("B-small.out", "w")

fin.readline()

lines = fin.readlines()



for j, line in enumerate(lines):
    line = line.split()
    s = int(line[1])
    p = int(line[2])
    count = 0
    for k in line[3:]:
        k = int(k)
        base = int(k/3)
        rem = k % 3
        if base + min([1, rem]) >= p:
            count += 1
        elif base + min ([1, rem]) == p - 1 and s > 0 and k > 1:
            s -= 1
            count += 1
        else:
            continue
    
    fout.write('Case #' + str(j+1)+ ': ' + str(count) + '\n')

fout.close()    
