#fob = open("A-small-practice.in")
fob = open("A-small-attempt0.in")
res = open("res.out","w")
def vod(sign, table):
    for i in range(4):
        t = 0
        z = True
        for j in range(4):
            if table[i][j]==signs[sign] or "T":
                t+=1
            elif table[i][j]==signs[not sign]:
                z = False
                break
        if t==4:
            return
T = int(fob.readline())
f = fob.readlines()
fob.close()

signs = ["X","O"]

for case in range(T):
    winner = ''
    draw = []
    table = f[case*5:(case+1)*5][0:4]
    tables = [table,zip(*table)]

    for table in tables:
        for sign in [True,False]:
            for i in range(4):
                t = 0
                z = True
                for j in range(4):
                    if table[i][j]==signs[sign] or table[i][j]=="T":
                        t+=1
                    elif table[i][j]==signs[not sign]:
                        z = False
                        break
                if t==4:
                    winner = signs[sign]
                else:draw.append(z)
            t = 0
            
            for j in range(4):

                if table[j][j]==signs[sign] or table[j][j]=="T":
                    t+=1
                elif table[j][j]==signs[not sign]:
                    z = False
                    break
            if t==4:
                winner = signs[sign]
                break 
            
            t = 0       
            for j in range(4):

                if table[3-j][j]==signs[sign] or table[3-j][j]=="T":
                    t+=1
                elif table[3-j][j]==signs[not sign]:
                    z = False
                    break
            if t==4:
                winner = signs[sign]
                break  


            
            table = zip(*table)
    if winner != '': 
        string = "Case #"+str(case+1)+": "+winner+" won\n"
    else:
        if any(draw):
            string = "Case #"+str(case+1)+": Game has not completed\n"
        else:
            string = "Case #"+str(case+1)+": Draw\n"
    res.write(string)
res.close()



'''
Created on 12. apr. 2013

@author: nraw
'''
