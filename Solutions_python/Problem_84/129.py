import os
import os.path

def solve(picture):
    for y in range(len(picture)):
        for x in range(len(picture[y])):
            if picture[y][x] == "#":
                if y+1 >= len(picture):
                    return "Impossible"
                if x+1 >= len(picture[y]):
                    return "Impossible"
                if picture[y+1][x] != "#":
                    return "Impossible"
                if picture[y][x+1] != "#":
                    return "Impossible"
                if picture[y+1][x+1] != "#":
                    return "Impossible"
                picture[y][x] = "/"
                picture[y+1][x] = "\\"
                picture[y][x+1] = "\\"
                picture[y+1][x+1] = "/"
    picture = [''.join(x) for x in picture]
    return '\n'.join(picture)

def square(path):
    fin = open(path)
    out_path = os.path.splitext(path)[0] + ".sol"
    fout = open(out_path, "w")

    num_cases = int(fin.readline().strip())

    for i in range(num_cases):
        num_lines = int(fin.readline().strip().split()[0])
        picture = []
        for j in range(num_lines):
            picture.append(list(fin.readline().strip()))
        sol = solve(picture)
        fout.write("Case #%i:\n%s\n" % (i+1, sol))

    fout.close()
    fin.close()
