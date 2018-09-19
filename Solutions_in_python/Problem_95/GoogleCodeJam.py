mapping = {"a":'y',
           "b":"h",
           "c":"e",
           "d":"s",
           "e":"o",
           "f":"c",
           "g":"v",
           "h":"x",
           "i":"d",
           "j":"u",
           "k":"i",
           "l":"g",
           "m":"l",
           "n":"b",
           "o":"k",
           "p":"r",
           "q":"z",
           "r":"t",
           "s":"n",
           "t":"w",
           "u":"j",
           "v":"p",
           "w":"f",
           "x":"m",
           "y":"a",
           "z":"q",
           " ":" ",
           "3":"3",
           '\n':'\n',
           "30":"30",
           "0":"0"}

def main():
    inFile = open("A-small-attempt2.in", "r")
    inputStr = inFile.read()

    outFile = open("foo1.txt", "w")
    outputStr= ""
    n = 0
    for i in inputStr:
        outputStr += mapping[list(i)[0]]
        if mapping[list(i)[0]] == '\n':
            print >> outFile, "Case #" + str(n) + ":"
            print >> outFile, outputStr
            outputStr = ""
            n += 1
        
main()
