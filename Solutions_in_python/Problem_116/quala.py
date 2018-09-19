
def result(matrix):
    lines = matrix + zip(*matrix) + [[matrix[i][i] for i in range(4)]] + [[matrix[i][3-i] for i in range(4)]]
    for r in lines:
        if all(map(lambda x:x in 'XT', r)):
            return 'X won'
        elif all(map(lambda x:x in 'OT', r)):
            return 'O won'
    if any(map(lambda x:'.' in x, lines)):
        return 'Game has not completed'
    else:
        return 'Draw'
                        

f = open('A-large.in')
r = f.readlines()
w = open('A-large.out','w')
for i in range((len(r)+1)/5):
    w.write('Case #%s: %s\n' % (str(i+1), result(map(lambda x:x.strip(),r[5*i+1:5*i+5]))))
f.close()
w.close()
