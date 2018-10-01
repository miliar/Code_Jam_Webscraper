'''
Created on Apr 13, 2013

@author: ashishgaunkar
'''
GAME_LINES = 4

RESULT_STRINGS = {
          'X' : "X won",
          'O' : "O won",
          'D' : "Draw",
          'G_ON' : "Game has not completed"      
          }

x = ('X', 'T')
o = ('O', 'T')

def read_file(path, filename):
    lines = [line.strip() for line in open(path+ '/' +filename) if line != '\n']
    return lines

def write_file(path, filename, ops):
    with open (path+ '/' +filename, 'a') as f:
        for o in ops:
            f.write (o+'\n')
            
def organize(game):
    '''
    game is a set of given game. Four lines.
    this method will convert it to dictionary
    '''
    game_list = []
    for i,g in enumerate(game):
        gr = [g[0],g[1], g[2], g[3]]
        game_list += [gr]
    return game_list

def wild_card(c):
    return True if c == 'T' else 1 if c =='X' else 2 if c == 'O' else c
    
def solve(g):
    v = None
    #check diagonal
    v = test(g[0][0] , g[1][1] , g[2][2] , g[3][3])
    if not v : v = test(g[3][0] , g[2][1] , g[1][2] , g[0][3])
    
    #check Row
    if not v : v = test(g[0][0] , g[0][1] , g[0][2] , g[0][3])
    if not v : v = test(g[1][0] , g[1][1] , g[1][2] , g[1][3])
    if not v : v = test(g[2][0] , g[2][1] , g[2][2] , g[2][3])
    if not v : v = test(g[3][0] , g[3][1] , g[3][2] , g[3][3])
   
    #check Column
    if not v : v = test(g[0][0] , g[1][0] , g[2][0] , g[3][0])
    if not v : v = test(g[0][1] , g[1][1] , g[2][1] , g[3][1])
    if not v : v = test(g[0][2] , g[1][2] , g[2][2] , g[3][2])
    if not v : v = test(g[0][3] , g[1][3] , g[2][3] , g[3][3])
    
    #print g[0][0] , g[0][1] , g[0][2] , g[0][3]
    if v in ('X', 'O'):
        return RESULT_STRINGS[v]
    elif '.' in (g[0] + g[1] + g[2] + g[3]):
        return RESULT_STRINGS['G_ON']
    else:
        return RESULT_STRINGS['D']
    
def test(a, b, c, d):
#    print a,b,c,d
    v=None
    if a in x and b in x and c in x and d in x:
        v = 'X'
    elif a in o and b in o and c in o and d in o:
        v= 'O'
    return v

    
if __name__ == '__main__':
    actual_result = {}
    path = '/Users/ashishgaunkar/workspace/CodeJam/io/'+ 'tic-tac'
    ip_file = 'A-large.in'
    op_file = 'A-large-op'
    lines = read_file(path, ip_file)
    total = int(lines[0])
    i=0
    ops=[]
    while(i < total):
        #read and organize next game . each game has GAME_LINES number of lines
        start = i * GAME_LINES + 1
        i+=1
        n0, n1, n2, n3 = start, start+1, start+2, start+3
        l0, l1 , l2, l3 = lines[n0], lines[n1], lines[n2], lines[n3]
#        print l0, l1, l2, l3
        game_list = organize([l0, l1, l2, l3])
        #print game_list
        game_status = solve(game_list)
        ops += ["Case #{0}: {1}".format(i, game_status)]
    write_file(path, op_file, ops)
    
    
    