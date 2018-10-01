
inputData = """4
4 11111
1 09
5 110011
0 1"""

#inputData = open("C:/Documents and Settings/Yury/Downloads/A-small-attempt0.in").read()
inputData = open("C:/Documents and Settings/Yury/Downloads/A-large.in").read()

def calculate(text):
    Smax, line = text.split()
    extraPersons = 0
    persons = 0
    for i, c in enumerate(line):
        if i <= persons:
            persons = persons + int(c)
        else:
            extra = i - persons
            extraPersons = extraPersons + extra
            persons = persons + extra  + int(c)
    return extraPersons

def parse(text):
    array = text.split("\n")
    ncases = int(array[0])
    output = []
    for i in range(ncases):
        output.append("Case #%d: %d" % (i+1, calculate(array[i+1])))
    open("aout.txt", "wb").write("\n".join(output))
#    print "\n".join(output)

parse(inputData)

