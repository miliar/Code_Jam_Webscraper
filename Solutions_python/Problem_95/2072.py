f = open("google_speaking.txt")

fw = open("google_speaking_output.txt","w")


td ={"a":"y", "b":"h" ,"c":"e", "d":"s", "e":"o", "f":"c", "g":"v", "h":"x", "i":"d","j":"u", "k":"i",
     "l":"g", "m":"l", "n":"b", "o":"k", "p":"r","q":"z", "r":"t", "s":"n", "t":"w", "u":"j","v":"p",
     "w":"f", "x":"m", "y":"a", "z":"q"  }

n = int(f.readline())
caseNum = 0

for line in f:
    caseNum +=1
    output = ""
    for c in line:
        if c == " " :
            output += " "
        elif c in td:
            output += td[c]
    fw.write("Case #" + str(caseNum) + ": "+ output +"\n")