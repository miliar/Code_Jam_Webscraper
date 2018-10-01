f = open("in.txt", 'r')
w = open("out3.txt", 'w')
for i in range(int(f.readline())):
    line = f.readline()
    line = line.split()
    line[0] = int(line[0])
    line[1] = int(line[1])
    line[2] = int(line[2])
    winner = -1
    if line[0] == 1:
        winner = 1
    elif line[0] == 2:
        winner = int((line[1] >= 2 or line[2] >= 2) and line[1]*line[2] % 2 == 0)
    elif line[0] == 3:
        winner = int((line[1] >= 3 or line[2] >= 3) and line[1]*line[2] % 3 == 0 and line[1]*line[2] >= 6)
    elif line[0] == 4:
        winner = int((line[1] == 4 or line[2] == 4) and line[1]*line[2] >= 12)
    if winner == 1:
        w.write("Case #"+ str(i+1) + ": GABRIEL\n")
    else:
        w.write("Case #"+ str(i+1) + ": RICHARD\n") 
f.close()
w.close()
