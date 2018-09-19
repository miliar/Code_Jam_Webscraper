def main():
    inpfile = open("A-large.in", 'r')
    outfile = open('outfile', 'w')
    casenum = int(inpfile.readline().strip())
    for case in range(1, casenum + 1):
        line = inpfile.readline().strip().split()
        n = int(line[0])
        pd = int(line[1])
        pd = pd / 100.0
        pg = int(line[2])
        pos = False
        i = 1.0
        while i <= n:
            j = 0
            while j <= i:
                #print j/i
                if j/i == pd:
                    pos = True
                    break
                j += 1
            if pos == True:
                break
            i += 1
        if pg == 0.0 and pd > 0:
            pos = False
        if pg == 100:
            if pd != 1.0:
                pos = False
            
        if pos:
            out = "Possible"
        else:
            out = "Broken"
        
        
        result = "Case #" + str(case) + ": " + out + "\n"
        outfile.write(result)
    inpfile.close()
    outfile.close()

    
if __name__ == "__main__":
    main()
    
