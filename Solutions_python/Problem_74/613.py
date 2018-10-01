from string import strip

def main():
    file = open(raw_input("Select file for processing: "))
    numcases = int(file.readline())
    for i in range(1, numcases + 1):
        olocation = 1
        blocation = 1
        otime = 0
        btime = 0
        print "Case #" + str(i) + ": ",
        words = map(strip, file.readline().split(" "))
        numwords = len(words)
        for j in range(1, numwords, 2):
            if words[j] == 'O':
                dest = int(words[j+1])
                otime = otime + abs(dest - olocation)
                if otime < btime:
                    otime = btime
                olocation = int(words[j+1])
                otime = otime + 1
            elif words[j] == 'B':
                dest = int(words[j+1])
                btime = btime + abs(dest - blocation)
                if btime < otime:
                    btime = otime
                blocation = int(words[j+1])
                btime = btime + 1
        print max([otime, btime])
                

if __name__ == '__main__':
    main()
