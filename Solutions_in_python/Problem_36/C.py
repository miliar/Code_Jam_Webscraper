#!/usr/bin/python

targetStr = "welcome to code jam"
occurrences = 0

def processFile():
#    fh = open("welcome-to-code-jam.in.prac")
    fh = open("input.txt")
    lines=[]
    for line in fh.readlines():
        lines.append(line.strip())
    iterations = int(lines.pop(0))
    results = []
    for i in range(0,iterations):
        results.append(procStuff(lines))
    x = 1
    for i in results:
        result = "0000" + str(i)
        result = result[-4:]
        print "Case #%s: %s" % (str(x),result)
        x = x+1

def procStuff(lines):
    global targetStr
    global startLetter
    global occurrences
    occurrences = 0
    everything = []
    searchString = lines.pop(0)
    index = 0
    position = 0

    def findNumMatches(pos_search,searchedstr):
        global targetStr
        char = targetStr[pos_search]
        num_matches = 0
        for i in range(len(searchedstr)):
            if (searchedstr[i] == char):
                if (pos_search == len(targetStr) -1):
                    num_matches+=1
                else:
                    num_matches+= findNumMatches(pos_search+1, searchedstr[i:len(searchedstr)])
        return num_matches

    return findNumMatches(0,searchString)

if __name__ == "__main__":
    processFile()

