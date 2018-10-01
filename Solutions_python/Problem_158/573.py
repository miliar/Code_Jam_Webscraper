from _commons.data import init_logging
import logging


PROJECT_NAME = 'codejam2015d'
INPUT_FILE = '../data/' + PROJECT_NAME + '/D-small-attempt0.in'
OUTPUT_FILE = '../data/' + PROJECT_NAME + '/output.txt'

RIC = "RICHARD"
GAB = "GABRIEL"

# Initiate logger
init_logging(logging.INFO)
            
def omino_fucker(X, R, C):
    if X == 1:
        return GAB
    if R == 1:
        if X >= 3:
            return RIC
        else:
            return GAB if C % X == 0 else RIC
    if C == 1:
        if X >= 3:
            return RIC
        else:
            return GAB if R % X == 0 else RIC
    if R == 2:
        if C == 2:
            return RIC if X >= 3 else GAB
        if C == 3: 
            return RIC if X == 4 else GAB
        if C == 4:
            return RIC if X == 3 or X == 4 else GAB
    if C == 2:
        if R == 2:
            return RIC if X >= 3 else GAB
        if R == 3: 
            return RIC if X == 4 else GAB
        if R == 4:
            return RIC if X == 3 or X == 4 else GAB
    if R == 3:
        if C == 3:
            return RIC if X == 2 or X == 4 else GAB
        if C == 4:
            return GAB
    if C == 3:
        if R == 3:
            return RIC if X == 2 or X == 4 else GAB
        if R == 4:
            return GAB
    if C == 4 and R == 4:
        return RIC if X == 3 else GAB
    
            
with open(OUTPUT_FILE, 'w') as g:
    with open(INPUT_FILE) as f:
        n = int(f.readline())
        for i in range(n):
            X, R, C = [int(x) for x in f.readline().split()]
            print X, R, C
            logging.info('This is crap')
            print "Case #%s: %s" % (i + 1, omino_fucker(X, R, C))
            g.write("Case #%s: %s\n" % (i + 1, omino_fucker(X, R, C)))
            