def main():
    with open("C-large.in") as cin:
        ca = 0
        z = "welcome to code jam"
        T = int(cin.readline())
        for t in range(0, T):
            line = cin.readline()
            line = line[:len(line) - 1]
            dp = []
            for i in range(0, 21):
                dp.append([])
                for j in range(0, 510):
                    dp[i].append(0)

            lenz = len(z)
            lenline = len(line)
            for i in range(0, lenz):
                for j in range(0, lenline):
                    if line[j] == z[i]:
                        if i > 0:
                            for k in range(0, j):
                                if line[k] == z[i - 1]:
                                    dp[i][j] += dp[i - 1][k]
                                    dp[i][j] %= 10000
                        else:
                            dp[i][j] = 1

            ret = 0
            for i in range(0, lenline):
                ret += dp[lenz - 1][i]
            ret %= 10000

            ca += 1
            print "Case #%d: %d%d%d%d" %(ca, ret / 1000, ret % 1000 / 100, ret % 100 / 10, ret % 10)

if __name__ == "__main__":
    main()
