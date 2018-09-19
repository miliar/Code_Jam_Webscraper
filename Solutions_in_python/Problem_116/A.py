in_file = open('A-small-attempt2.in')
out_file = open('a.out', 'w')

def solver(linha):
    vazio = 0
    for x in range(len(linha)):
        if(linha[x].find('.') != -1):
            vazio = 1
        if((linha[x][0] == linha[x][1] or linha[x][0] == 'T' or linha[x][1] == 'T') and (linha[x][1] == linha[x][2] or linha[x][2] == 'T') and (linha[x][2] == linha[x][3] or linha[x][3] == 'T')):
            if(linha[x][0] != '.'):
                if(linha[x][0] != 'T'):
                    return "%s won" % linha[x][0]
                else:
                    return "%s won" % linha[x][1]
                
        if((linha[0][x] == linha[1][x] or linha[0][x] == 'T' or linha[1][x] == 'T') and (linha[1][x] == linha[2][x] or linha[2][x] == 'T') and (linha[2][x] == linha[3][x] or linha[3][x] == 'T')):
            if(linha[0][x] != '.'):
                if(linha[0][x] != 'T'):
                    return "%s won" % linha[0][x]
                else:
                    return "%s won" % linha[1][x]
                

    if((linha[0][0] == linha[1][1] or linha[0][0] == 'T' or linha[1][1] == 'T') and (linha[1][1] == linha[2][2] or linha[2][2] == 'T') and (linha[2][2] == linha[3][3] or linha[3][3] == 'T')):
        if(linha[0][0] != '.'):
            if(linha[0][0] != 'T'):
                return "%s won" % linha[0][0]
            else:
                return "%s won" % linha[1][1]

    if((linha[0][3] == linha[1][2] or linha[0][3] == 'T' or linha[1][2] == 'T') and (linha[1][2] == linha[2][1] or linha[2][1] == 'T') and (linha[2][1] == linha[3][0] or linha[3][0] == 'T')):
        if(linha[0][3] != '.'):
            if(linha[0][3] != 'T'):
                return "%s won" % linha[0][3]
            else:
                return "%s won" % linha[1][2]

    if(vazio == 0):
        return "Draw"
    else:
        return "Game has not completed"


cases = int(in_file.readline())

for n in range(1, cases+1):
    valores = [in_file.readline(),in_file.readline(),in_file.readline(),in_file.readline()]
    answer = solver(valores)
    in_file.readline()
    out_file.write("Case #%d: %s\n" % (n, answer))


in_file.close()
out_file.close()
