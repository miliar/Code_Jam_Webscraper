def checkline(line):
    if (line[0]=='X' or line[0]=='T') and (line[1]=='X' or line[1]=='T') \
       and (line[2]=='X' or line[2]=='T') and (line[3]=='X' or line[3]=='T'):
        return 'X won'
    if (line[0]=='O' or line[0]=='T') and (line[1]=='O' or line[1]=='T') \
       and (line[2]=='O' or line[2]=='T') and (line[3]=='O' or line[3]=='T'):
        return 'O won'
def solve():
    first = f.readline()
    second = f.readline()
    third = f.readline()
    fourth = f.readline()
    f.readline()
    x=checkline(first)
    if x:
        return x
    x=checkline(second)
    if x:
        return x
    x=checkline(third)
    if x:
        return x
    x=checkline(fourth)
    if x:
        return x
    x=checkline([first[0],second[0],third[0],fourth[0]])
    if x:
        return x
    x=checkline([first[1],second[1],third[1],fourth[1]])
    if x:
        return x
    x=checkline([first[2],second[2],third[2],fourth[2]])
    if x:
        return x
    x=checkline([first[3],second[3],third[3],fourth[3]])
    if x:
        return x
    x=checkline([first[0],second[1],third[2],fourth[3]])
    if x:
        return x
    x=checkline([first[3],second[2],third[1],fourth[0]])
    if x:
        return x
    if '.' in first or '.' in second or '.' in third or '.' in fourth:
        return 'Game has not completed'
    else:
        return 'Draw'

with open('A-large.in','r') as f:
    o = open('A-large.out','w')
    for z in range(int(f.readline())):
        output = 'Case #'+str(z+1)+': '+solve()+'\n'
        o.write(output)
    o.close()
