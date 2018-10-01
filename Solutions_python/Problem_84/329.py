def check(mp, i, j, r, c):
    if i + 1 >= r:
        return False
    if j + 1 >= c:
        return False
    if mp[i][j] == '#' and mp[i + 1][j] == '#' and mp[i][j + 1] == '#' and mp[i + 1][j + 1] == '#':
        return True
    else:
        return False


def main():
    inpfile = open("A-large.in", 'r')
    outfile = open('outfile', 'w')
    casenum = int(inpfile.readline().strip())
    for case in range(1, casenum + 1):
        line = inpfile.readline().strip().split()
        r = int(line[0])
        c = int(line[1])
        mp = []
        for i in range(r):
            line = inpfile.readline().strip()
            mp.append(line)
        #print mp
        
        can = True
        i = 0
        while i < r:
            j = 0
            while j < c:
                if mp[i][j] == '#':
                    if check(mp,i,j,r,c):
                        mp[i] = mp[i][0:j]+'/\\'+mp[i][j+2:]
                        mp[i+1] = mp[i+1][0:j]+'\\/'+mp[i+1][j+2:]
                    else:
                        can = False
                    if not can:
                        break
                j += 1
                if not can:
                    break
            i += 1
        
        #print mp
        #print can
        if not can:
            result = "Case #" + str(case) + ": " + "\n" + "Impossible" + "\n" 
            outfile.write(result)
        else:
            result = "Case #" + str(case) + ": " + "\n"
            outfile.write(result)
            for i in range(r):
                result = mp[i] + "\n"
                outfile.write(result)
        
    inpfile.close()
    outfile.close()

    
if __name__ == "__main__":
    main()
    
