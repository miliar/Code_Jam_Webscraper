

input = open("input.txt", "r")
output = open("output.txt", "w")


cases = int(input.readline())

for case in range(cases):
    line = input.readline()
    data = line.split(" ")
    smax = int(data[0])
    sum = 0
    needed = 0

    for i in range(len(data[1])):
        if i > smax:
            break
        current = int(data[1][i])
        if current > 0:
            if i > sum:
                needed += (i - sum)
                sum += needed
            sum += current

    output.write("Case #%d: %d\n" % (case + 1, needed))
