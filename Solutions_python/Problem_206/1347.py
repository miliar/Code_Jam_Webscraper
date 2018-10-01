def main():
    with open("A-large.in", 'r') as file, open("output.txt", 'w') as out:
        cases = file.readline()

        for case in range(int(cases)):
            line = file.readline()
            d = int(line.split(' ')[0])
            n = int(line.split(' ')[1])

            p = []
            s = []
            t = []
            for i in range(n):
                line = file.readline()
                p.append(int(line.split(' ')[0]))
                s.append(int(line.split(' ')[1]))
                t.append((d - p[i]) / s[i])

            time = max(t)
            ans = d / time

            out.write("Case #" + str(case+1) + ": " + str(ans) + "\n")

if __name__ == "__main__":
    main()
