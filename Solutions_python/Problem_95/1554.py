import sys

translator = {"a" : "y",
"b" : "h",
"c" : "e",
"d" : "s",
"e" : "o",
"f" : "c",
"g" : "v",
"h" : "x",
"i" : "d",
"j" : "u",
"k" : "i",
"l" : "g",
"m" : "l",
"n" : "b",
"o" : "k",
"p" : "r",
"q" : "z",
"r" : "t",
"s" : "n",
"t" : "w",
"u" : "j",
"v" : "p",
"w" : "f",
"x" : "m",
"y" : "a",
"z" : "q"}
n = sys.stdin.readline()
googlese=sys.stdin.readline()
i = 1
string = ""
for g in googlese:
    if g in translator:
        string = string + translator[g]
    elif (g == "\n"):
        print("Case #" + str(i) + ": " + string)
        i = i + 1
        string = ""
    else:
        string = string + g
            
     
