import re

CHECK_V_X = re.compile(".*X.{3}X.{3}X.{3}X")
CHECK_H_X = re.compile("^(....)*XXXX")
CHECK_D_X = re.compile("^(X.{4}X.{4}X.{4}X.{3}|.{3}X.{2}X.{2}X.{2}X)")
CHECK_V_O = re.compile(".*O.{3}O.{3}O.{3}O")
CHECK_H_O = re.compile("^(....)*OOOO")
CHECK_D_O = re.compile("^(O.{4}O.{4}O.{4}O|.{3}O.{2}O.{2}O.{2}O)")

CHECK_UNFIN = re.compile(r'\.')

def checkgame(lline):
    xline = lline.replace("T","X")
    if CHECK_V_X.findall(xline) or CHECK_H_X.findall(xline) or CHECK_D_X.findall(xline):
        return "X won"
    oline = lline.replace("T","O")
    if CHECK_V_O.findall(oline) or CHECK_H_O.findall(oline) or CHECK_D_O.findall(oline):
        return "O won"
    if CHECK_UNFIN.findall(lline):
        return "Game has not completed"
    return "Draw"

if __name__ == "__main__":
    for case in xrange(1,input()+1):
        lline = ""
        for l in xrange(4):
            lline += raw_input()
        print "Case #%d: %s" % (case,checkgame(lline))
        try:
            raw_input()
        except EOFError:
            pass
