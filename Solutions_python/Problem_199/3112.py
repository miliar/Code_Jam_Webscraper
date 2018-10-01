import math

def find(pancake, k):
    result = 0
    l = len(pancake)
    i = 0
    while i < l - k + 1:
        if pancake[i] == "+":
            i += 1
        else:
            result += 1
            temp = pancake[:i]
            for j in range(k):
                if pancake[i + j] == "+":
                    temp += "-"
                else:
                    temp += "+"
            temp += pancake[i + k:]
            pancake = temp
            i += 1
    for j in range(i, l):
        if pancake[j] == "-":
            return "IMPOSSIBLE"
    return str(result)

inputfilename = "A-large.in"
fin = open(inputfilename, "r")
outputfilename = "oversized_pancake_flipper_output.txt"
fout = open(outputfilename, "w")
t = fin.readline()
t = int(t)
for i in xrange(1, t+1):
	line = fin.readline().split(" ")
	s = line[0]
	k = int(line[1])
	result = "Case #" + str(i) + ": " + find(s, k) + '\n'
	fout.write(result)

fin.close()
fout.close()
