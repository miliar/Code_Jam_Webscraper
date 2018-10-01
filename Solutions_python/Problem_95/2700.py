import os
os.chdir("//Users//moomeowroar//Desktop//Google Code Jam//")
f = open("A-small-attempt0.in" ,  'r')
result = open("result.txt" ,  'w')
count = 0
lineList = []
translatedList = []
finalList = []
translate = {"n":"b" , "f":"c" , "i":"d" , "c":"e" , "w":"f" , "l":"g" , "b":"h" , "k":"i" , "u":"j" , "o":"k" , "m":"l" , "x":"m" , "s":"n" , "e":"o" , "v":"p" , "z":"q" , "p":"r" , "d":"s" , "r":"t" , "j":"u" , "g":"v" , "t":"w" , "h":"x" , "a":"y" , "q":"z" , "y":"a"}
for line in f:
    if count <1:
        numberOfCases = line
        count += 1
    else:
        line=line.strip()
        line=line.split()
        lineList.append(line)
count = 1
num = 0
translatedWord = ""

for line in lineList:
    for word in line:
        for letter in word:
            translatedWord = translatedWord + translate[letter]
        translatedList.append(translatedWord)
        translatedWord = ""
    finalList.append(translatedList)
    translatedList=[]

while count <= int(numberOfCases):
    result.write("Case #" + str(count) + ": ")
    for word in finalList[int(count)-1]:
        result.write(word + " ")
    count += 1
    result.write("\n")
result.close()
