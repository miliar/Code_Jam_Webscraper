file = open("A-large.in","r")
lines = file.readlines()[1:]
file.close()
temp = []
results = []


def flip(pancakes):
    flipped = ""
    for pancake in pancakes:
        if pancake == "+":
            flipped+="-"
        else:
            flipped+="+"
    return flipped

for line in lines:
    [pancakes,k] = line.split(" ")
    k = int(k)
    flips = 0
    for i in range(len(pancakes)-k+1):
        if pancakes[i] == "-":
            flips += 1
            pancakes = pancakes[:i]+ flip(pancakes[i:i+k])+pancakes[i+k:]
    if "-" in pancakes[len(pancakes)-k:]:
        temp.append("IMPOSSIBLE")
    else:
        temp.append(flips)
   
file = open("A-large.out","w")
for i in range(len(temp)):
    results.append("Case #{0}: {1}\n".format(i+1,temp[i]))
file.writelines(results)
file.close()

