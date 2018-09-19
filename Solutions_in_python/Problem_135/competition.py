
def checking_case (ans1,game1,ans2,game2):
    c = 0
    d = 0
    for j in range (0,4):
        if (game1[ans1][j] in game2[ans2]):
            c+=1
            d = game1[ans1][j]
    return c,d

            
def result (c,n,index):
    output = ''
    if c == 1:
        output = str(n)
    elif c > 1:
        output = 'Bad magician!'
    else :
        output = 'Volunteer cheated!'
    return "Case #"+str(index)+": "+output+"\n"


fin = open("A-small-attempt0.in","r")
fout = open("Aproblem.txt","w")   
n = int(fin.readline())
game1 = []
game2 = []
ans1=0
ans2=0
for i in range (0,n):
    game1 = []
    game2 = []
    ans1 = int(fin.readline())
    for j in range(0,4):
        s = fin.readline()
        s = s[:-1]
        a = list(map(int,s.split()))
        game1.append(a)
    ans2 = int(fin.readline())
    for j in range(0,4):
        s = fin.readline()
        s = s[:-1]
        b = list(map(int,s.split()))
        game2.append(b)
    c,d = checking_case(ans1-1,game1,ans2-1,game2)
    fout.write(result(c,d,i+1))
fout.close()
















    
    
