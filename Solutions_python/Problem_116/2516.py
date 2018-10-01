def check_win(vals):
    xvals = []
    ovals = []
    for val in vals:
        if val == "T":
            xvals.append("X")
            ovals.append("O")
        else:
            xvals.append(val)
            ovals.append(val)
    if xvals[0]=="X" and xvals[1]=="X" and xvals[2]=="X" and xvals[3]=="X":return "X"
    elif ovals[0]=="O" and ovals[1]=="O" and ovals[2]=="O" and ovals[3]=="O": return "O"
    else: return None
    
def judge(mat,c):
    #rows
    for i in range(4):
        vals = [mat[i][0],mat[i][1],mat[i][2],mat[i][3]]
        winner = check_win(vals)
        if winner:
            return "Case #%s: %s won" % (c,winner)
            
    #cols        
    for i in range(4):
        vals = [mat[0][i],mat[1][i],mat[2][i],mat[3][i]]
        winner = check_win(vals)
        if winner:
            return "Case #%s: %s won" % (c,winner)
            
    #diagdown
    vals = [mat[0][0],mat[1][1],mat[2][2],mat[3][3]]
    winner = check_win(vals)
    if winner:
        return "Case #%s: %s won" % (c,winner)
        
    #diagup
    vals = [mat[0][3],mat[1][2],mat[2][1],mat[3][0]]
    winner = check_win(vals)
    if winner:
        return "Case #%s: %s won" % (c,winner)
        
    
    for row in mat:
        if '.' in row:
            return "Case #%s: Game has not completed" % (c)
            
    return "Case #%s: Draw" % (c)        
def process(c, lst):
    f = open("A-large.out","w")
    for i in range(int(c)):
        start = i*5
        mat = [lst[start],lst[start+1],lst[start+2],lst[start+3]]
        result = judge(mat,i+1)
        print result
        f.write(result)
        if i<int(c)-1:
            f.write("\n")
    f.close()
        
def main():
    f = open("A-large.in")
    conts = f.read()
    f.close()
    contslist = conts.split("\n")
    cases = contslist[0]
    contslist = contslist[1:]
    print contslist
    process(cases, contslist)

if __name__ == "__main__":
    main()