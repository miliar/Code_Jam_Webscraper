'''
SpeakingInTongues
Uso: python Main.py file_in file_out

@author: Jose Antonio Perdiguero Lopez
@param -h --help: Muestra esta documentacion
'''

import sys
import getopt

'''
Input
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv


Output
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up
'''

_DIC = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o',
        'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u',
        'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k',
        'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w',
        'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a',
        'z':'q', ' ':' '}

class CodeJamError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

def toGooglerese(s):
    global _DIC
    
    result = ''
    for c in s:
        result += _DIC[c]
        
    return result

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        return 2
    
    # Procesar opciones
    for o, _ in opts:
        if o in ("-h", "--help"):
            print __doc__
            return 0
        
    # Procesar argumentos 
    try:
        if (len(args) == 0):
            raise CodeJamError("Uso incorrecto, para mostrar ayuda use --help")
        elif (len(args) < 2):
            fout = sys.stdout
        elif (len(args) < 3):
            fout = open(args[1], 'w')
        
        fin = open(args[0], 'r')
    except IOError, ioe:
        print "Error de entrada-salida"
        print ioe
    except CodeJamError, cje:
        print cje
            
    # Cuerpo principal
    lineas = int(fin.readline())
    
    for i in range(1, lineas+1):
        print >>fout, "Case #{:d}: {}".format(i, toGooglerese(fin.readline().strip()))
    
    # Cerrar flujos
    fin.close()
    if (len(args) == 3):
        fout.close()

if __name__ == '__main__':
    sys.exit(main())