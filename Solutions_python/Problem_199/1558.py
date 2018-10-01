def flip(array, index, s):
    for i in range(s):
        array[index + i] = not array[index + i]

fileName = "A-large.in"
f = open(fileName, 'r')

outputName = "A-large-out.txt"
output = open(outputName, 'w')

line = f.readline()
T = int(line)

for t in range(T):
    line = f.readline()
    line = line.split()
    pancakes = line[0]
    s = int(line[1])
    l = len(pancakes)
    array = [False for i in range(l)]
    for i in range(l):
        if pancakes[i] == "+":
            array[i] = True
        else:
            array[i] = False
    index = 0
    flips = 0
    while index + s <= l:
        if array[index]:
            index += 1
        else:
            flip(array, index, s)
            flips += 1
    
    impossible = False
    while index < l:
        if not array[index]:
            impossible = True
            break
        index += 1
    
    res = ""
    if impossible:
        res = "IMPOSSIBLE"
    else:
        res = str(flips)
        
    print("Case #{}: {}".format(t+1, res))
    output.write("Case #{}: {}".format(t+1, res))
    output.write("\n")
    
output.close()