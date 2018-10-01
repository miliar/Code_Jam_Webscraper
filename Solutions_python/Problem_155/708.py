__author__ = 'rsadykov'

def readInputs():
    input_file = open("A-large.in", "r")
    text = input_file.read()
    lines = text.split("\n")
    return lines

def processInputs(lines):
    out_file = open("out_file.txt", "w")
    for i in range(1, len(lines)):
        if(lines[i] == ""):
            continue
        relevant_line = lines[i].split(" ")[1]
        out_file.write("Case #" + str(i) + ": " + processInput(relevant_line) + "\n")

def processInput(line):
    total = 0
    needed = 0
    for i in range(0, len(line)):
        #print str(total) + " " + str(needed) + " " + str(i)
        if i > total:
            needed+=1
            total+=1 + int(line[i])
        else:
            total += int(line[i])
    return str(needed)

lines = readInputs()
processInputs(lines)

