

def resolve(line):
    standing = 0
    added = 0
    for required, shy in enumerate(line):
        if required > standing:
            added += required - standing
            standing += required - standing
        standing += int(shy)
    return added

with open("A.in") as f:
    lines = f.readlines()

#n_tests = int(raw_input())

with open("A.out",'w') as f:
    for i,line in enumerate(lines[1:]):
        #line = raw_input()
        f.write("Case #{}: {}\n".format(i+1,resolve(line.split()[1])))
