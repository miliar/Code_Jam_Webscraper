def FlipCakes(s):
    new = ""
    for p in s:
        if p == '+':
            new += "-"
        elif p == '-':
            new += "+"
    return new

def SerialTry(p, n, case):
    print("[+] Trying Case #" + str(case))

    counter = 0
    while ('-' in p) and (counter < 10):
        index = p.find("-", 0)
        if (index != -1) and (index <= len(p) - n):
            p = p.replace(p[index:n+index], FlipCakes(p[index:n+index]), 1)
            print(str(index) + ":" + p)
        counter += 1

    if counter >= 10:
        out = "Case #" + str(case) + ": IMPOSSIBLE"
        print(out)
        f2.write(out + '\n')
    else:
        out = "Case #" + str(case) + ": " + str(counter)
        print(out)
        f2.write(out + '\n')

    '''new = p
    for i in range(0, len(new), 1):
        if p[i] == '-':
            new = FlipCakes(p[i:n+i]) + new[n+i:len(p)-n+i]
    print(new)'''


filename = "C:\\Users\\duckarcher\\Downloads\\A-small-attempt1.in"
f = open(filename)
f2 = open(filename.replace(".in", ".out"), 'w')
case = 1
for line in f:
    line = line.strip('\n')
    if ("+" in line) or ("-" in line):
        print(line)
        pancakes = line.split(" ")[0]
        flipper_size = int(line.split(" ")[1])
        SerialTry(pancakes, flipper_size, case)
        case += 1