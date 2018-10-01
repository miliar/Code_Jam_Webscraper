from sys import stdin

def get_answer():
    parts = stdin.readline().strip().split()
    r = int(parts[0])
    c = int(parts[1])
    m = []
    for i in range(r):
        m.append([el for el in stdin.readline().strip()])
    res = []
    for i in range(r):
        row = []
        prev_letter = None
        for j in range(c):
            if m[i][j] != "?":
                if prev_letter is None:
                    row.extend([m[i][j] for l in range(j + 1)])
                    prev_letter = m[i][j]
                else:
                    row.append(m[i][j])
                    prev_letter = m[i][j]
            if m[i][j] == "?" and prev_letter is not None:
                row.append(prev_letter)
        res.append(row)
    if res[0] == []:
        cr = 0
        for i in range(r):
            if res[i] != []:
                cr = i
                break
        res[0] = res[cr]
    for i in range(r):
        if res[i] != []:
            res[i] = "".join(res[i])
        if res[i] == []:
            res[i] = res[i - 1]
    return "\n".join(res)

def main():
    t = int(stdin.readline().strip())
    for i in range(t):
        print "Case #{0}:".format(i + 1)
        print get_answer()


if __name__ == "__main__":
    main()
