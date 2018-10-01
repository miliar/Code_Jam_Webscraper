#! python3

DATA_FILE = "A-large"

def main():
    with open(DATA_FILE + ".in") as in_file:
        with open(DATA_FILE + ".out", "w") as fout:
            cases = int(in_file.readline())
            for x in range(cases):
                line = in_file.readline().replace('\n', '')
                cakes, K = line.split()
                K = int(K)
                cakes = [True if c == '+' else False for c in cakes]
                flips = 0

                for i in range(len(cakes) - K + 1):
                    if cakes[i] == False:
                        cakes[i:i+K] = [not c for c in cakes[i:i+K]]
                        flips += 1

                if sum(cakes) != len(cakes):
                    flips = "IMPOSSIBLE"

                fout.write("Case #{0}: {1}\n".format(x + 1, flips))

if __name__ == "__main__":
    main()
