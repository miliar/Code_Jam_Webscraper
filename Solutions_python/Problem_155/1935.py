__author__ = 'eunice'

class StandingOvation:
    def solve(self, f, resf):
        t = int(f.readline())
        for i in range(0, t):
            res = "Case #" + str(i + 1) + ": "
            line = f.readline().split()
            smax = int(line[0])
            slist = list(line[1])
            standing = 0
            friends = 0
            for s in range(0, smax+1):
                if standing >= s:
                    standing += int(slist[s])
                else:
                    friends += 1
                    standing += 1 + int(slist[s])
            resf.write(res + str(friends) + '\n')



if __name__ == "__main__":
    f = open('A-large.in', 'r')
    resf = open('A-large.out', 'w')
    # f = open('test.txt', 'r')
    # resf = open('result.out', 'w')
    StandingOvation().solve(f, resf)