diag=[]
rows=[]
col=[]

def check_win(test_row,sym):
    ans=0
    for i in range(0,4):
        if test_row[i]==sym or test_row[i]=='T':
            ans+=1
            
            
    if ans ==4:
        return True
    else:
        return False

def game_draw(rs):
    res=0
    for i in range(0,4):
        if rs[i]=='X' or rs[i]=='O' or rs[i]=='T':
            res+=1
    return res
    
        
def solve(r1,r2,r3,r4):
    
    c1=[]
    c2=[]
    c3=[]
    c4=[]
    d1=[]
    d2=[]
    rows=[]
    col=[]
    diag=[]
    c1.append(r1[0]),c1.append(r2[0]),c1.append(r3[0]),c1.append(r4[0])
    col.append(c1)
    c2.append(r1[1]),c2.append(r2[1]),c2.append(r3[1]),c2.append(r4[1])
    col.append(c2)
    c3.append(r1[2]),c3.append(r2[2]),c3.append(r3[2]),c3.append(r4[2])
    col.append(c3)
    c4.append(r1[3]),c4.append(r2[3]),c4.append(r3[3]),c4.append(r4[3])
    col.append(c4)
    d1.append(r1[0]),d1.append(r2[1]),d1.append(r3[2]),d1.append(r4[3])
    diag.append(d1)
    d2.append(r1[3]),d2.append(r2[2]),d2.append(r3[1]),d2.append(r4[0])
    diag.append(d2)
    rows.append(r1)
    rows.append(r2)
    rows.append(r3)
    rows.append(r4)
    

    
    #check if X wins
    result=False
    for i in range (0,4):
        result=(check_win(col[i],'X'))
        if result ==True:
            return "X won"
            

    result=False    
    for i in range (0,4):
        result = check_win(rows[i],'X')
        if result == True:
            return "X won"
            
    result=False    
    for i in range (0,2):
        result = check_win(diag[i],'X')
        if result == True:
            return "X won"
            
    
    result=False
    #check if O wins

    for i in range (0,4):
        result=(check_win(col[i],'O'))
        if result ==True:
            return "O won"
            

    result=False  
    for i in range (0,4):
        result = check_win(rows[i],'O')
        if result == True:
            return "O won"
            
    result=True
    
    for i in range (0,2):
              
        result = check_win(diag[i],'O')
        if result == True:
            return "O won"
            

    #check if game is a draw
    draw=0
    for i in range(0,4):
        draw+=game_draw(rows[i])
            
           
    if draw == 16:
            return "Draw"
    else:
        return "Game has not completed"
    
            

   
    
    
def test_tic():
            ls = open('Alarge.in','r').read()
            lines = ls.split('\n')
            no_of_case = int(lines[0])
            
            line_count = 0
            for j in range(1,no_of_case+1):
                line_count+=1
                r1=lines[line_count]
                line_count+=1
                r2=lines[line_count]
                line_count+=1
                r3=lines[line_count]
                line_count+=1
                r4=lines[line_count]
                print "Case #%d: " % (j), str(solve(r1,r2,r3,r4))
                line_count+=1
                
