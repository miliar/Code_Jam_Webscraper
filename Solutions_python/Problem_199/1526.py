import numpy as np


# Input
file = "A-large.in"
text = [line.rstrip() for line in open(file, 'r')]
cases = text[0]
values = text[1:]


# Functions
def calcflips(pc, sze):
    N = len(pc)
    ct = 0
    for idx in range(N):
        if pc[idx] == "-" and idx <= N-sze:
            for jdx in range(sze):
                if pc[idx+jdx] == "-":
                    pc[idx+jdx] = "+"
                else:
                    pc[idx+jdx] = "-"
            ct += 1

    if "-" in pc:
        return "IMPOSSIBLE"
    else:
        return ct
        

# Run cases
results = []
for case in values:
    pc, sze = case.split(" ")
    sze = int(sze)
    pc = list(pc)
    this = calcflips(pc, sze)
    if this == "IMPOSSIBLE":
        this = calcflips(list(reversed(pc)), sze)
    results.append(this)
    
print(results)
    

# Output
file = open("output.txt", 'w')
for i in range(len(results)):
    file.write("Case #{:d}: {}\n".format(i+1, results[i]))