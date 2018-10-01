f = open('A-large.in', 'ro')
g = open('A-large.out', 'w')
input = f.readlines()
casecnt = input[0]
game = []

for i in range(int(casecnt)):
    game.append(list(input[i*5+1].rstrip()+input[i*5+2].rstrip()+input[i*5+3].rstrip()+input[i*5+4].rstrip()))

f.close()

cnt=0

for case in game:
    cnt += 1
    map={'.' : 0, 'T' : 1, 'X' : 2, 'O' : 3}
    out=[]
    for i in xrange(4):
        out.append(map[case[i*4]]*map[case[i*4+1]]*map[case[i*4+2]]*map[case[i*4+3]])
        out.append(map[case[i]]*map[case[i+4]]*map[case[i+8]]*map[case[i+12]])
        out.append(map[case[0]]*map[case[5]]*map[case[10]]*map[case[15]])
        out.append(map[case[3]]*map[case[6]]*map[case[9]]*map[case[12]])
    if map['X']**3 in out or map['X']**4 in out:
        g.write('Case #'+str(cnt)+': X won \n')
    elif map['O']**3 in out or map['O']**4 in out:
        g.write('Case #'+str(cnt)+': O won \n')
    elif map['.'] in out:
        g.write('Case #'+str(cnt)+': Game has not completed \n')
    else:
        g.write('Case #'+str(cnt)+': Draw \n')

g.close()
