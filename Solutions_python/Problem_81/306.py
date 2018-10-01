import re
import sys

def solve_case(line, fin):
    parts = line.split()
    N = int(parts[0])
    wins, games = [], []
    for i in range(N):
        line = fin.readline().strip()
        wins.append([1 if c == '1' else 0 for c in line])
        games.append([0 if c == '.' else 1 for c in line])
    wp = [sum(w) * 1.0 / sum(g) for w, g in zip(wins, games)]

    owp = []
    for i in range(N):
        xowp, nowp = 0.0, 0
        for j in range(N):
            if j != i and games[j][i] == 1:
                xowp += sum(wins[j][:i] + wins[j][i+1:]) * 1.0 / sum(games[j][:i] + games[j][i+1:])
                nowp += 1
        owp.append(xowp/nowp)

    oowp = []
    for i in range(N):
        x, n = 0.0, 0
        for j in range(N):
            if j != i and games[j][i] == 1:
                x += owp[j]
                n += 1
        oowp.append(x/n)

    rpi = [0.25 * w + 0.5 * o + 0.25 * oo for (w, o, oo) in zip(wp, owp, oowp)]
    return rpi

def test():
    inpath, outpath = 'sample.in', 'sample.out'
    fin = open(inpath)
    line = fin.readline().strip()
    line = fin.readline().strip()
    line = fin.readline().strip()
    fin.close()

def main(inpath, outpath):
    fin = open(inpath)
    T = int(fin.readline().strip())
    fout = open(outpath, 'w')
    for t in range(T):
        # print >>fout, 'Case #%d: %s' % (t+1, solve_case(fin.readline().strip(), fin))
        print >>fout, 'Case #%d:\n%s' % (t+1, '\n'.join(
                '%.12g' % r for r in solve_case(fin.readline().strip(), fin)))
    fin.close()
    fout.close()

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
