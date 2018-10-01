#!/usr/bin/python

def test_fila(c,tab,pieza):
        if (tab[c].count('X') + tab[c].count('.')) == 0:
                pieza[0] = 'O'
                return False
        elif (tab[c].count('O') + tab[c].count('.')) == 0:
                pieza[0] = 'X'
                return False
        return True

def test_columna(c,tab,pieza):
        nuarray = [tab[0][c],tab[1][c],tab[2][c],tab[3][c]]
        if (nuarray.count('X') + nuarray.count('.')) == 0:
                pieza[0] = 'O'
                return False
        elif (nuarray.count('O') + nuarray.count('.')) == 0:
                pieza[0] = 'X'
                return False
        return True

def test_diagonal(c,tab,pieza):
        if c == 0:
                nuarray = [tab[0][0],tab[1][1],tab[2][2],tab[3][3]]
        else:
                nuarray = [tab[0][3],tab[1][2],tab[2][1],tab[3][0]]
        if (nuarray.count('X') + nuarray.count('.')) == 0:
                pieza[0] = 'O'
                return False
        elif (nuarray.count('O') + nuarray.count('.')) == 0:
                pieza[0] = 'X'
                return False
        return True

def main():
        r = input()
        contador = 1
        for i in range(int(r)):
                
                continuar = True
                nodraw = False
                foo = 1
                tablero = [[foo for i in range(4)] for j in range(4)]
                pieza = ['T']
                
                for c in range(4):
                        leido = raw_input()
                        for f in range(4):
                                tablero[c][f] = leido[f]
                                if tablero[c][f] == '.':
                                        nodraw = True
                c = 0
                while continuar and c < 4:
                        continuar = test_fila(c,tablero,pieza)
                        c = c + 1
                c = 0
                while continuar and c < 4:
                        continuar = test_columna(c,tablero,pieza)
                        c = c + 1
                c = 0
                while continuar and c < 2:
                        continuar = test_diagonal(c,tablero,pieza)
                        c = c + 1
                if continuar and nodraw:
                        print("Case #" + str(contador) + ": Game has not completed\n")
                elif continuar:
                        print("Case #" + str(contador) + ": Draw\n")
                else:
                        print("Case #" + str(contador) + ": " + pieza[0] + " won\n")
                contador = contador + 1

main()
