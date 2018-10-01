import sys

def main():
    fname = sys.argv[1]
    with open(fname) as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if i == 0:
            n_cases = int(line)
            assert(len(lines) == n_cases + 1)
        else:
            line = line[:-1]
            last = 0
            save = ""
            candidate = ""
            reduced = ""
            for j, c in enumerate(line):
                d = int(c)
                if d > last:
                    save += candidate
                    candidate = c
                    reduced = str(d - 1) if (d - 1) > 0 else ""
                elif d == last:
                    candidate += c
                    reduced += str(9)
                else:
                    save += reduced + "9" * (len(line) - j)
                    candidate = ""
                    break
                last = d
            save += candidate
            print("Case #%i: %s" % (i, save))


if __name__ == "__main__":
    main()
