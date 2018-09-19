# tic-tac-toe-tomek
# TECTEC - Google CodeJam entry
# April 13 2013

def read_words(filename, Z):
    '''
    converts a file to a list
    '''
    
    words = []
    for line in filename:
            words.append(line.strip())
    return words

def CheckWin(Q, target): # do a really stupid compare thing b/c python is dumb
 
    for j in range(4): 
        if (Q[4*j] == target or Q[4*j] == 'T')and (Q[4*j+1] == target or Q[4*j+1] == 'T') and (Q[4*j+2] == target or Q[4*j+2] == 'T') and (Q[4*j+3] == target or Q[4*j+3] == 'T'):
            return True #rows check
            
    for k in range(4): 
        if (Q[k] == target or Q[k] == 'T')and (Q[k+4] == target or Q[k+4] =='T') and (Q[k+8] == target or Q[k+8] == 'T')and (Q[k+12] ==target or Q[k+12] == 'T'):
            return True #columns check
            
    if (Q[0] == target or Q[0] == 'T') and (Q[5] == target or Q[5] == 'T') and (Q[10] == target or Q[10] =='T')and (Q[15] == target or Q[15] == 'T'):
        return True # left-to-right check
        
    if (Q[3] == target or Q[3] =='T') and (Q[6] == target or Q[6] =='T') and (Q[9] == target or Q[9] == 'T')and (Q[12] == target or Q[12] =='T'):
        return True #right - to-left check
    
    return False   


                
def determine_outcome(a_list):
    
    if CheckWin(a_list, 'X') == True:
        return "X won"

    elif CheckWin(a_list, 'O') == True:
        return "O won"
    else:
        for i in range(16):
            if a_list[i] == '.':
                return "Game has not completed"

            elif i ==15:        
                return "Draw"

filename=open("test.txt", 'r')
T= int(filename.readline())


scenario = []
total = []
total =  read_words(filename, T)

for k in range(T):
    sString1 = '' #make two test strings b/c python is dumb

    sString1+=total[5*k]
    sString1+=total[5*k+1]
    sString1+=total[5*k+2]
    sString1+=total[5*k+3]

    outcome = determine_outcome(sString1)
    casenum = k+1
    
    print "Case #" + str(casenum) +": "+outcome


