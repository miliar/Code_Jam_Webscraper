f = open("A-small-attempt1.in", "r")
out = open("out.txt", "w")
testn = int(f.readline())

for t in range(1, testn+1):
    s = f.readline().split()
    smax = int(s[0])
    people = s[1]
    standing = 0
    need = 0
    for i in range(smax+1):
        if int(people[i]) == 0:
            continue
        if standing >= i:
            standing += int(people[i])
        else:
            need += i - standing
            standing += need
            standing += int(people[i])

    out.write("Case #" + str(t) + ": " + str(need))
    out.write('\n')

f.close()
out.close()
