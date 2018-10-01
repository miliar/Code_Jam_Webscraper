def tile(picture):
    picture = picture.strip().split("\n")
    for x in range(len(picture[0]) - 1):
        for y in range(len(picture) - 1):
            if picture[y][x] == "#" and picture[y + 1][x] == "#" and picture[y][x + 1] == "#" and picture[y + 1][x + 1] == "#":
                picture[y] = picture[y][:x] + "/\\" + picture[y][x + 2:]
                picture[y + 1] = picture[y + 1][:x] + "\/" + picture[y + 1][x + 2:]
    for line in picture:
        if line.find("#") != -1:
            return ["Impossible"]
    result = ""
    return picture
                
f = file("input.txt")
lines = f.readlines()
line = 0
for i in range(int(lines[line])):
    line += 1
    case = ""
    for j in range(int(lines[line].split(" ")[0])):
        line += 1
        case += lines[line]
    res = tile(case)
    print "Case #" + str(i + 1) + ":"
    for j in res:
        print j
