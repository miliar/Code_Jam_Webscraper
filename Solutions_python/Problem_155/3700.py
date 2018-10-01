infile = open("A-small-attempt0.in.txt", "r")
outfile = open("output.txt", "w")
case = infile.readline()
lines = infile.readlines()
case = 0
for shy in lines:
    case +=1
    max_lvl = int(shy[0])
    add = 0
    total = int(shy[2])
    for i in range (3, max_lvl+3):
        lvl = i-2
        num = int(shy[i])
        if total>=lvl:
            total += num
        else:
            add = add+lvl-total
            total = total + num + lvl - total
    outfile.write("Case #{0}: {1}\n".format(case, add))
infile.close()
outfile.close()
