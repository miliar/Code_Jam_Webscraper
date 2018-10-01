'''
Created on 14/04/2013

@author: Adam
'''

results = []

def failsdown(current, lawn, r, c):
    while r < len(lawn) - 1:
        r += 1
        if int(lawn[r][c]) > current:
            return True
    return False

def failsup(current, lawn, r, c):
    while r > 0:
        r -= 1
        if int(lawn[r][c]) > current:
            return True
    return False

def failsright(current, lawn, r, c):
    while c < len(lawn[0]) - 1:
        c += 1
        if int(lawn[r][c]) > current:
            return True
    return False

def failsleft(current, lawn, r, c):
    while c > 0:
        c -= 1
        if int(lawn[r][c]) > current:
            return True
    return False
    
# If any square has no path (up/down/left/right) where
# ALL squares in that path are less than the current square,
# then this lawn is impossible.
def checklawn(lawn):\
    # Check each square
    for r in range(0, len(lawn)):
        for c in range(0, len(lawn[0])):
            current = int(lawn[r][c])
            # Short-circuit checking when we find a successful exit path
            if failsleft(current, lawn, r, c) or failsright(current, lawn, r, c):
                if failsup(current, lawn, r, c) or failsdown(current, lawn, r, c):
                    results.append('NO')
                    return    
    results.append('YES')
            
infile = open('qb_input_easy.txt', 'r')
cases = int(infile.readline())

for case in range(0,cases):
    lawn = []
    nm = infile.readline().split(' ')
    n = int(nm[0])
    m = int(nm[1])
    for i in range(0,n):
        lawn.append(infile.readline().split(' '))
    if n == 1 or m == 1:
        results.append('YES')
    else:
        checklawn(lawn)
        
outfile = open('output.txt', 'w')
count = 0
for result in results:
    count += 1 
    outfile.write('Case #' + str(count) + ': ' + result + '\n')

infile.close()    
outfile.close()