with open('A-large.in') as file:
    ain=file.readlines()
cases=int(ain[0])
line=1
wfile=open('out.txt','w')
for case in range(cases):
    DN=ain[line].split()
    line+=1
    D=int(DN[0])
    N=int(DN[1])
    maxt=0
    for i in range(N):
        KS=ain[line].split()
        line+=1
        Ki=int(KS[0])
        Si=int(KS[1])
        value=(D-Ki)/float(Si)
        if value>maxt:
            maxt=value
    wfile.write("Case #{}: {:.6f}\n".format(case+1,D/maxt))
wfile.close()
