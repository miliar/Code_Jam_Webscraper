
INPUT_FILE = "./A-large.in"
OUTPUT_FILE = "./A-large.out"

if __name__ == '__main__':
    with open(INPUT_FILE, "r") as fin, open(OUTPUT_FILE, "w") as fout:
        T = int(fin.readline())
        for case_i in range(1, T + 1):
            D, N = map(int, fin.readline().split())
            ans = 0
            for _ in range(N):
                k, s = map(int, fin.readline().split())
                ans = max(ans, (D - k) / s)
            ans = D / ans
            print('Case #{}: {}'.format(case_i, ans), file = fout)