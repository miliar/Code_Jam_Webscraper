import re

if __name__ == '__main__':
    fin = open("./test.in", "r")
    fout = open("./test.out", "w")

    words = []

    line = fin.readline().split(" ")
    wlen = int(line[0])
    dictsize = int(line[1])
    N = int(line[2])

    for w in range(0, dictsize):
        words.append(fin.readline().replace("\n", ""))

    for test in range(0, N):
        msg = fin.readline().replace("\n", "")
        total = 0
        par = 0
        com = []
        tmp = []

        for char in msg:
            if char == "(":
                par = 1
            elif char == ")":
                par = 0
                com.append(tmp)
                tmp = []
            else:
                if par == 0:
                    com.append([char])
                else:
                    tmp.append(char)

        #print(com)
               
        for word in words:
            match = -1
            pos = 0
            for l in word:
                #print( "sprawdzam czy " + l + " jest na liscie o indeksie " + str(pos))
                itm = com.__getitem__(pos)
                try:
                    itm.index(l)
                    #print( "jest!" )
                except ValueError:
                    #print("nie ma?")
                    match = 0
                    break
                if match == 0:
                    break
                if pos == len(word)-1 and match == -1:
                    #print("slowo dopasowane")
                    match = 1
                    break
                pos += 1
            if match == 1:
                total += 1
                #print("trafienie")

        fout.write("Case #" + str(test+1) + ": " + str(total) + "\n")