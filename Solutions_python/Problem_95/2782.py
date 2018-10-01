GOOGLERESE_TO_ENGLIGH_MAP_DICT = {  'a':'y',
                                    'b':'h',
                                    'c':'e',
                                    'd':'s',
                                    'e':'o',
                                    'f':'c',
                                    'g':'v',
                                    'h':'x',
                                    'i':'d',
                                    'j':'u',
                                    'k':'i',
                                    'l':'g',
                                    'm':'l',
                                    'n':'b',
                                    'o':'k',
                                    'p':'r',
                                    'q':'z',
                                    'r':'t',
                                    's':'n',
                                    't':'w',
                                    'u':'j',
                                    'v':'p',
                                    'w':'f',
                                    'x':'m',
                                    'y':'a',
                                    'z':'q',
                                    ' ':' ',
                                    '\n':'\n',
                                        }
def runProgram(fileName) :
    fileIn  = open(fileName,"r")
    fileOut = open(fileName.replace(".in",".out"),"w") 
    numTestCases = int(fileIn.next())
    i   = 1
    googleExprInputs = {}
    while i <= numTestCases :
        googleExpr  = fileIn.next()
        englishExpr = ''.join(map(GOOGLERESE_TO_ENGLIGH_MAP_DICT.get,googleExpr))
        fileOut.write("Case #%d: %s" % (i,englishExpr))
        i += 1
    fileIn.close()
    fileOut.close()
