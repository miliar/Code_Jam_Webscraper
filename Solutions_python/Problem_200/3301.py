f = open("input.in", "r")
out = open("out.out", "w")

cases = int(f.readline())
num = 0
for line in f:
    num+=1
    cons = False
    first=-1
    mark = -1
    res = ""
    
    if len(line)==2:
        out.write("CASE #%d: %s" % (num, line))
        continue

    for i in range(len(line)-2):
        if line[i]<line[i+1]:
            first = -1
            cons = False
            continue
        if line[i]==line[i+1]:
            if first > i or first == -1:
                first = i
            cons = True
            continue
        mark = i
        break
    if mark == -1:
        out.write("CASE #%d: %s" % (num, line))
        continue

    if cons:
        res = line[:first] + str(int(line[first])-1) + '9'*(len(line)-first-2)
    else:
        res = line[:mark] + str(int(line[mark])-1) + '9'*(len(line)-mark-2)
    out.write("CASE #%d: %s\n" % (num, res.lstrip('0')))
out.close()
f.close()
