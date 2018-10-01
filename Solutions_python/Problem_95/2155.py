import sys

al="abcdefghijklmnopqrstuvwxyz"

inputs = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
          "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
          "de kr kd eoya kw aej tysr re ujdr lkgc jv",
          "y qee"]

outputs = ["our language is impossible to understand",
          "there are twenty six factorial possibilities",
          "so it is okay if you want to just give up",
          "a zoo"]

outputstring = "".join(outputs).replace(" ","")
inputstring = "".join(inputs).replace(" ","")

translate_table = {}
for i,c in enumerate(inputstring):
    translate_table[c] = outputstring[i]
translate_table["z"] = "q"

#for k in sorted(translate_table):
#    print k, " = ", translate_table[k]



with open(sys.argv[1], "r") as f:
    lines = f.read().splitlines()

T = int(lines[0])

outlines=[]
i=1
case = 1

while i<len(lines):
    outline = ""
    for c in lines[i]:
        if c == " ":
            outline += " "
        else:
            outline += translate_table[c]
    outlines.append(outline)
    i += 1


with open("out", "w") as f:
    for i,outline in enumerate(outlines):
        f.write("Case #{0}: {1}\n".format(i+1, outline))




