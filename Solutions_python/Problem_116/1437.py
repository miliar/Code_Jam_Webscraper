
def check2(v):
    n = v[0]|v[1]|v[2]|v[3];
    if n & 1 == 1: return -1 #empty
    return (n>>2) % 3 #1:X 2:O 0:MIX

def play(result):
    global incomplete
    global winner
    if result == -1: incomplete = 1
    if result == 1: winner = 'X'
    if result == 2: winner = 'O'
 
# read the source
f = open('A-large.in')
ncases = int(f.readline())
ret = ''
cmap = '.TXO'
mat = [[0 for x in range(4)] for y in range(4)]
for icase in range(ncases):
    ret += 'Case #{}: '.format(icase+1)
    
    winner = ''
    incomplete = 0
    for row in range(4):
        line = str(f.readline())
        for col in range(4):
            mat[row][col] = 1 << cmap.find(line[col]);
    
    for row in range(4):
        play(check2(mat[row]))
   
    for col in range(4):
        play(check2([x[col] for x in mat]))
    
    play(check2([mat[i][i] for i in range(4)]))
    play(check2([mat[i][3-i] for i in range(4)]))
    
    if winner: ret += winner + ' won'
    else: 
        if incomplete: ret += 'Game has not completed'
        else: ret += 'Draw' 
    
    ret += '\n'
    
    f.readline()

f.close()

# write the solution
f = open('out.txt', 'w')
f.write(ret)
f.close()
print 'done'