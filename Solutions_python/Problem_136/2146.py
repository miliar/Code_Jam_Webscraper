input = open("in.txt",'r')
output = open('out.txt','w')

def solve(C,F,X):
    r = 2;
    ans = X/r
    d = C/r
    while(((X/(r+F))+d)<ans):
        ans = (X/(r+F))+d
        d = (C/(r+F))+d
        r = r+F       
    return str(ans);

case = 0
for lino,line in enumerate(input.readlines()):       
    if(lino == 0):
        continue  
    C,F,X = map(float,line.split())                
    output.write("Case #%d:"%lino + " "+solve(C,F,X)+"\n")    
output.close()
    

