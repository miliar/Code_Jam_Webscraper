import sys

filename = sys.argv[1]
print "Using file", filename
inputf = open(filename, 'r')
outputname = filename[:-2] + "out"
outputf = open(outputname, 'w')

def read(inp, pos):
    arr = []
    curr = ""
    while pos < len(inp):
        if inp[pos] == ' ' or inp[pos] == "\n":
            if curr != "":
                arr.append(curr)
                curr = ""
        elif inp[pos] == '(':
            newpos, readed = read(inp, pos + 1)
            arr.append(readed)
            pos = newpos
        elif inp[pos] == ')':
            if curr != "":
                arr.append(curr)
            return (pos, arr)
        else:
            curr += inp[pos]           
        pos += 1
    return arr

def calc(arr, caract):
    val = 1
    print arr[0]
    val *= float(arr[0])
    if len(arr) > 1:
        if arr[1] in caract:
            val *= calc(arr[2], caract)
        else:
            val *= calc(arr[3], caract)
    return val

cases = int(inputf.readline())
print cases, "test cases"
for case in range(1, cases + 1):
    outputf.write("Case #" + str(case) + ":\n")
    print "Case", case
    
    dectreelen = int(inputf.readline())
    #print dectreelen
    inp = ""
    for _ in range(dectreelen):
        inp = inp + inputf.readline()
    #print inp
    arr = read(inp, 0)
    #print arr
        
    animlen = int(inputf.readline())
    #print animlen
    animals = []
    for _ in range(animlen):
        animal = inputf.readline().split()
        animals.append((animal[0], animal[1], animal[2:])) 
    #print animals
    for a in animals:
        val = 1.0
        if len(arr) >= 1:
            print a[2]
            val = calc(arr[0], a[2])
        outputf.write("{0:.7f}".format(val) + "\n")
    
    
inputf.close()
outputf.close()
