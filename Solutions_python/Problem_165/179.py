import sys

in_file = open(sys.argv[1], "r")

out_file = open("output.out", "w")

t = int(in_file.readline())

for i in range(t):
    params = in_file.readline().split(' ')

    r = int(params[0])
    c = int(params[1])
    w = int(params[2])

    tempc = c
    turns = 0
    while tempc > w:
        tempc -= w
        turns += 1
    turns *= r
    if tempc == w:
        turns += r + w - 1
    else:
        turns += w

    out_file.write("Case #" + str(i + 1) + ": " + str(turns))

    out_file.write("\n")

in_file.close()
out_file.close()
