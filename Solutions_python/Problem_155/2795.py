

def getCases(fileName):
    with open(fileName) as f:
        content = f.readlines()
    lines = [x.strip() for x in content if (x and len(x.strip())>0)]
    if len(lines)-1 != int(lines[0]):
        raise Exception("Oups")
    return lines
    
def ovation(list, ind, standed):
    delta = 0
    added = 0
    delta = ind - standed
    if delta > 0:
        standed += delta
        added += delta
    standed += int(list[ind])
    return [standed, added]
    
file = "./input.txt"
l = getCases(file)
for i in range(1,len(l)):
    s = l[i].split(" ")
    standed = 0
    totalAdded = 0
    for j in range(0,int(s[0])+1):
        ret = ovation(s[1], j, standed)
        standed = ret[0]
        totalAdded += ret[1]
    with open("out.txt","a") as fi:
        fi.write("Case #{0}: {1}\n".format(i, totalAdded))

