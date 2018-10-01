
def logic(inp):
    counter = 0
    parts = inp.split(" ")
    pancakes = list(parts[0])
    ksize = int(parts[1])
    for i in range(len(pancakes) - ksize + 1):
        if pancakes[i] == "-":
            #flip k
            counter += 1
            for j in range(ksize):
                if (pancakes[i+j] == "-"):
                    pancakes[i+j] = "+"
                else:
                    pancakes[i+j] = "-"

    for i in range(len(pancakes)):
        if pancakes[i] == "-":
            return "IMPOSSIBLE"
    return counter

filename = "file.o"
f = open(filename, 'r')
wf = open(filename.split(".")[0]+".a", 'w')
cases = int(f.readline())
for i in range(cases):
    ans = logic(f.readline())
    wf.write("Case #" + str(i+1) + ": " + str(ans) + "\n")
f.close()
wf.close()
