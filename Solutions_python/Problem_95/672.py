outfile = "output.txt"

def popinput(input):
    return int(input.readline().split()[0])


def solve(file):
    input = open(file, 'r')
    output = open(outfile, 'w')
    cases = popinput(input)
    for i in range(cases):
        output.write("Case #%(number)d: %(answer)s\n" % {"number":i + 1, "answer":solvecase(input)})

  

def solvecase(input):
    line = input.readline().trim()
    


def buildcode(codetext, plaintext, dict):
    for i in range(len(codetext)):
        if codetext[i] not in dict:
            dict[codetext[i]] = plaintext[i]

code = {}
buildcode("ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand", code)
buildcode("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities", code)
buildcode("de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up", code)

      
