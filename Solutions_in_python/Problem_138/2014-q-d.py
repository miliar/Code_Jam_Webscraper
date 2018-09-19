class Solver(object):
    def __init__(self, p1_blocks, p2_blocks):
        self.p1_blocks = sorted(p1_blocks)
        self.p2_blocks = sorted(p2_blocks)

    def deceitful_war_points(self):
        points = 0
        j = 0
        for i in range(len(self.p1_blocks)):
            if self.p1_blocks[i] > self.p2_blocks[j]:
                points += 1
                j += 1
                if j == len(self.p2_blocks):
                    break
        return points

    def war_points(self):
        p1_blocks_r = sorted(self.p1_blocks, reverse=True)
        p2_blocks_r = sorted(self.p2_blocks, reverse=True)
        points = 0
        j = 0
        for i in range(len(p1_blocks_r)):
            if p1_blocks_r[i] > p2_blocks_r[j]:
                points += 1
            else:
                j += 1
        return points


f = open('test.txt')
num_cases = int(f.readline())

out = open('out.txt', 'w')

for i in range(num_cases):
    f.readline()
    p1_blocks = [float(n) for n in f.readline().strip().split(' ')]
    p2_blocks = [float(n) for n in f.readline().strip().split(' ')]
    s = Solver(p1_blocks, p2_blocks)
    out.write("Case #%d: %d %d\n" % (i+1, s.deceitful_war_points(), s.war_points()))