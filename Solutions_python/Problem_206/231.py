#! python3

DATA_FILE = "A-large"

def main():
    with open(DATA_FILE + ".in") as in_file:
        with open(DATA_FILE + ".out", "w") as fout:
            cases = int(in_file.readline())
            for x in range(cases):
                line = in_file.readline().replace('\n', '')
                D, N = [int(n) for n in line.split()]
                max_time = 0
                for i in range(N):
                    line = in_file.readline().replace('\n', '')
                    K, S = [int(n) for n in line.split()]
                    horse_max = (D - K) / S
                    if horse_max > max_time:
                        max_time = horse_max
                speed = D / max_time

                print("Case #{}: {}".format(x + 1, speed), file=fout)

if __name__ == "__main__":
    main()
