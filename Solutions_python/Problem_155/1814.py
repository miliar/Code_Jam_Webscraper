f = open('input')
writing = open("output", "w")

n = 0
for i, line in enumerate(f):
    if (i == 0):
        n = int(line)
    else:
        standing = 0
        need = 0
        parsed = line.strip().split()
        s_max = int(parsed[0])
        aud = parsed[1]
        for x in range(0, s_max + 1):
            if (standing < x):
                need += (x - standing)
                standing = x + int(aud[x])
            else:
                standing += int(aud[x])
        writing.write("Case #" + str(i) + ": " + str(need) + "\n")
f.close()
writing.close()
