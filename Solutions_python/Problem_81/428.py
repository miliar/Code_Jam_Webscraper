def solve(problem):
    wp = []
    wpgen = []
    n = int(problem[0])
    for i in range(1,n+1):
        print (problem[i])
        wp.append(wper(problem[i]))
        wpcurr = []
        for j in range(1,i):
            if(problem[i][j-1] != '.'):
                wpcurr.append(wout(problem[j],i))
        for j in range(i+1,n+1):
            if(problem[i][j-1] != '.'):
                wpcurr.append(wout(problem[j],i))
        wpgen.append(sum(wpcurr)/(problem[i].count("0")+problem[i].count("1")))
    print (wp)
    print (wpgen)
    rpi = []
    for i in range(0,n):
        k = 0
        s = 0
        oowp = 0
        for j in range(0,n):
            if(problem[i+1][j] != '.'):
                s = s + wpgen[j]
                k = k + 1
        oowp = s/k
        print ("oowp:" + str(oowp))
        rpi.append(0.25*wp[i] + 0.5*wpgen[i] + 0.25*oowp)
    print (rpi)
    return rpi
        
    
def wper(team):
    wins = team.count("1")
    losses = team.count("0")
    wp = wins/(wins+losses)
    return wp


def wout(team,x):
    wins = team[0:x-1].count("1") + team[x:].count("1")
    losses = team[0:x-1].count("0") + team[x:].count("0")
    wp = wins/(wins+losses)
    return wp


def actualsolve():
    with open('in.txt', 'r') as infile: # this will automatically close the file
            stuff = infile.readlines()
    
    print (stuff[0])
    ptr = 1

    for i in range(1,int(stuff[0])+1):
       
        instance = []
        for j in range(0,int(stuff[ptr])+1):
            if(stuff[ptr+j][-1:] == "\n"):
                instance.append((stuff[ptr+j][:-1]))
            else:
                instance.append((stuff[ptr+j][:]))
        print (instance)
        answer = solve(instance)
        ptr = ptr + int(stuff[ptr]) + 1
        print ("---------")
        print 
        print (answer)
        for x in answer:
            print(x)
        with open('out.txt', 'a') as scorefile:
            scorefile.write("Case #" + str(i) + ":\n")
            for x in answer:
                x = str(x)
                scorefile.write("{e}\n".format(e=x[0:14]))


actualsolve()



#p = ['4','.11.','0.00','01.1','.10.']
#p = ['3','.10','0.1','10.']
#solve(p)