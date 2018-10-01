
def main():
    with open('A-large.in') as f:
        with open('output.txt', 'w+') as o:
            f.readline()
            casenum = 1
            for line in f:
                parts = line.split()
                standing = 0
                sl = 0
                added = 0
                for c in parts[1]:
                    if standing >= sl:
                        standing += int(c)
                    else:
                        diff = sl - standing
                        added += diff
                        standing += int(c) + diff
                    sl += 1
                o.write("Case #" + str(casenum) + ": " + str(added) + "\n")
                casenum += 1

if __name__ == "__main__":
    main()
