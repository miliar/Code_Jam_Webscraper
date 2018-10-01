
def INfile(fileName):

    LINES    = []
    input_fh    =  open(fileName, "r")
    for line in input_fh:
             LINES.append(line.split())
    input_fh.close()

    return LINES
    

def solve(data):

    S        = []
    UP       = 0
    Tfriends = 0
    lenData  = len(data)

    for i in range(lenData):
        S.append([i,int(data[i:i+1])])

    for i in range(lenData):
        CurrentShyNumber   = S[i][1]
        CurrentShyIndex    = S[i][0]
        if CurrentShyIndex <= UP or CurrentShyNumber == 0:
            UP += CurrentShyNumber
        else:
            newFriends = 0
            while CurrentShyIndex > UP + newFriends:
                  newFriends += 1
            UP += (CurrentShyNumber + newFriends)      
            Tfriends += newFriends
            
    return Tfriends


################ Main #########################################

INfilename    = "A-large.in"#"test.in"
OUTfilename   = "StandingOvation.out"

tableIN       =  INfile(INfilename)  
Ncases        =  int(tableIN[0][0])
tableIN.pop(0)

output_fh     =  open(OUTfilename, "w")

for i in range(Ncases):
    friends    =  solve(tableIN[i][1])
    lineOut    =  "Case #%d: %s" % (i+1, friends)
    output_fh.write(lineOut+'\n')

output_fh.close()
