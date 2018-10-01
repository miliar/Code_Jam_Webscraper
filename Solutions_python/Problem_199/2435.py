def solve_a(path="E:\\Users\\Neta\\Desktop\\dashyts\\googlejam.txt"):
    f = open(path, "r")
    T = f.readline()
    T = int(T)
    #path_out = "E:\\Users\\Neta\\Desktop\\dashyts\\googlejamSOL.txt"
    #fout = open(path_out, "w")
    case = 0
    for i in range(T):
        line = f.readline()
        case = case + 1
        count = 0
        args = line.split(" ")
        K = int(args[1])
        panLine = args[0]
        #print(panLine)
        for j in range(len(panLine) - K + 1):
            if panLine[j] == "+":
                #print(panLine)
                continue
            elif panLine[j] == "-":
                count = count + 1
                newPanLine = panLine[0:j]
                for c in range(K):
                    if panLine[j+c] == "+":
                        newPanLine = newPanLine + "-"
                    elif panLine[j+c] == "-":
                        newPanLine = newPanLine + "+"
                panLine = newPanLine + panLine[j+K:]
                #print(panLine)
        if "-" in panLine:
            print("Case #" + str(case) +": IMPOSSIBLE")
        else:
            print("Case #" + str(case) +": "+ str(count))
