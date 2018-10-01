__author__ = 'Levan Kasradze'


def dist(s1, s2):
    dp = [[float('+inf') for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
    dp[0][0] = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j]
                if i > 0 and s1[i - 1] == s1[i]:
                    dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j+1] + 1)
                if j > 0 and s2[j - 1] == s2[j]:
                    dp[i+1][j+1] = min(dp[i+1][j+1], dp[i+1][j] + 1)
    return dp[len(s1)][len(s2)]


fin = open('a.in')
fout = open('a.out', 'w')
T = int(fin.readline())
for t in range(1, T + 1):
    fout.write('Case #' + str(t) + ': ')
    n = int(fin.readline())
    words = []
    for i in range(n):
        line = fin.readline().strip()
        words.append(line)

    res = dist(words[0], words[1])
    if res != float('+inf'):
        fout.write(str(res) + '\n')
    else:
        fout.write('Fegla Won\n')

fin.close()
fout.close()