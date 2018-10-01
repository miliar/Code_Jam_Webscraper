from sys import argv

def flip(pancake):
    return ["+" if x == "-" else "-" for x in pancake]

def flips(pancake, flip_size):
    pancake = list(pancake)
    flips = 0
    while pancake and (pancake[0] == "+" or len(pancake) >= flip_size):
        if pancake[0] == "+":
            pancake.pop(0)
        else:
            pancake = flip(pancake[:flip_size]) + pancake[flip_size:]
            flips += 1

    if len(pancake) == 0:
        return flips
    else:
        return "IMPOSSIBLE"

def write_cases(func, filename):
    with open(filename) as fi, open(filename.split(".")[0] + ".out", "w") as fo:
        for i in range(1, int(fi.readline().strip())+1):
            pancake, num = fi.readline().strip().split()
            print("Case #{}: {}".format(i, func(pancake, int(num))), file=fo)

def print_cases(func, filename):
    with open(filename) as fi:
        for i in range(1, int(fi.readline().strip())+1):
            line = fi.readline().strip()
            pancake, num = line.split()
            print("{} -> {}".format(line, func(pancake, int(num))))

if __name__ == "__main__":
    write_cases(flips, argv[1])

