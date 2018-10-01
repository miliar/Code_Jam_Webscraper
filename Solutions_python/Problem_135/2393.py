import sys

def main():
    f = open(sys.argv[1], "r")
    t = int(f.readline().strip())

    f2 = open(sys.argv[2], "w")

    for i in range(t):
        f2.write("Case #"+str(i+1)+": ")
        a1 = int(f.readline().strip())
        lines = []
        for j in range(4):
            lines.append([int(elem) for elem in f.readline().strip().split()])
        cand = set(lines[a1-1])

        a2 = int(f.readline().strip())
        lines = []
        for j in range(4):
            lines.append([int(elem) for elem in f.readline().strip().split()])
        cand2 = set(lines[a2-1])

        ins = cand & cand2

        if len(ins) > 1:
            f2.write("Bad magician!")
        elif len(ins) == 0:
            f2.write("Volunteer cheated!")
        else:
            for elem in ins:
                f2.write(str(elem))
                break
        f2.write("\n")

if __name__ == "__main__":
    main()
    
