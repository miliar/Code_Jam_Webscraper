def ifRow(row, n):
    return row == '1'*n


def yes(w,h,i,j,Tlst):
    row = ''
    for x in range(w):
        row += Tlst[x][j]
    #print "row", row
    
        
    col = ''
    for x in range(h):
        col += Tlst[i][x]   
    #print "col", col
    
    return ifRow(row, w) or ifRow(col, h)
    
def check(Tlst,w,h):
    i = 0
    for row in Tlst:
        j = 0
        for elem in row:
            
            if elem == '1':
                if not yes(w,h,i,j,Tlst):
                    return False
            j += 1
        i += 1
    return True


def main():
    inpfile = open("B-small-attempt0.in", 'r')
    outfile = open('outfile', 'w')
    casenum = int(inpfile.readline().strip())
    for case in range(1, casenum + 1):
        S = ""
        line = inpfile.readline().strip()
        linelst = line.split()
        w = int(linelst[0])
        h = int(linelst[1])
        #print w,h
        
        Tlst = []
        for x in range(w):
            line = inpfile.readline().strip()
            linelst = line.split()
            #print linelst
            
            Tlst.append(linelst)
        
        #print Tlst
        #for row in Tlst:
            #for elem in row:
                #1
        
        #print yes(w,h,0,0,Tlst)
        if check(Tlst,w,h):
            S = 'YES'
        else:
            S = 'NO'
        
        result = "Case #" + str(case) + ": " + str(S)+"\n"
        print result
        
        outfile.write(result)
    inpfile.close()
    outfile.close()




if __name__ == "__main__":


    main()
    

    
    