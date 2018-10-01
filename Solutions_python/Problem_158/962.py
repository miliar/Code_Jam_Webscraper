__author__ = 'Tony'
def WTF(inty):
    f = open('my.out','a')
    f.write(inty+'\n') # python will convert \n to os.linesep
    f.close()

with open("D-small-attempt0.in") as f:
    content = f.readlines()
numOfTests = content[0]

for testNum in xrange(1,int(numOfTests)+1):
    game = content[testNum].split()
    x = int(game[0])
    rows = int(game[1])
    columns = int(game[2])
    if (x == 1):
        if ((rows >= 1)&(columns >= 1)):
            WTF("Case #"+str(testNum)+": GABRIEL")
        else:
            WTF("Case #"+str(testNum)+": RICHARD")
    if (x == 2):
        if ((rows*columns)%2 == 0)&((rows >= 1)&(columns >= 1)):
            WTF("Case #"+str(testNum)+": GABRIEL")
        else:
            WTF("Case #"+str(testNum)+": RICHARD")
    if (x == 3):
        if ((rows*columns)%3 == 0)&(((rows >= 3)&(columns >= 2))|((rows >= 2)&(columns >= 3)))&((rows >= 1)&(columns >= 1)):
            WTF("Case #"+str(testNum)+": GABRIEL")
        else:
            WTF("Case #"+str(testNum)+": RICHARD")
    if (x == 4):
        if ((rows*columns)%4 == 0)&(((rows >= 4)&(columns >= 3))|((rows >= 3)&(columns >= 4)))&((rows >= 1)&(columns >= 1)):
            WTF("Case #"+str(testNum)+": GABRIEL")
        else:
            WTF("Case #"+str(testNum)+": RICHARD")