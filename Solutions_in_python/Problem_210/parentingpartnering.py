from solution import Solution

class Parenting(Solution):
    def parse_input(self):
        with open(self.input_file) as f:
            t = int(f.readline().strip())
            self.times = []
            for _ in range(t):
                ac, aj = [int(c) for c in f.readline().split()]
                c_times = []
                for _ in range(ac):
                    c_times.append([int(c) for c in f.readline().split()])
                j_times = []
                for _ in range(aj):
                    j_times.append([int(c) for c in f.readline().split()])
                self.times.append((c_times, j_times))

    @staticmethod
    def find_extra_breaks(t, breaks):
        print "t", t
        breaks.sort()
        breaks = breaks[::-1]
        for i, b in enumerate(breaks):
            t -= b
            print "b", b
            if t <= 0:
                return i+1

    def calculate(self, c_times, j_times):
        print "------"
        intervals = [[c_start, c_end, 0] for c_start, c_end in c_times] + [[j_start, j_end, 1] for j_start, j_end in j_times]
        intervals.sort(key=lambda x: x[0])
        cur_interval = [0, 0, -1]
        big_intervals = []
        breaks = [[], []]
        big_breaks = []
        for interval in intervals + [[1440, 1440, -1]]:
            if interval[2] != cur_interval[2]:
                big_intervals.append(cur_interval)
                cur_interval = interval[:]
                continue
            breaks[interval[2]].append(interval[0]-cur_interval[1])
            cur_interval[1] = interval[1]
        big_intervals = big_intervals[1:]
        if big_intervals[0][2] == big_intervals[-1][2]:
            breaks[big_intervals[0][2]].append(big_intervals[0][0]+1440-big_intervals[-1][1])
            if len(big_intervals)>1:
                a = big_intervals.pop(0)
                b = big_intervals.pop(-1)
                big_intervals.append([b[0], 1440+a[1], a[2]])
            else:
                big_intervals = [[0,1440, big_intervals[0][2]]]
        changes = len(big_intervals)
        changes -= changes % 2
        jtime = sum(interval[1]-interval[0] for interval in big_intervals if interval[2] == 0)
        ctime = sum(interval[1]-interval[0] for interval in big_intervals if interval[2] == 1)
        extra = 0
        if jtime > 720:
            extra = self.find_extra_breaks(jtime-720, [b for b in breaks[0]])
        if ctime > 720:
            extra = self.find_extra_breaks(ctime-720, [b for b in breaks[1]])
        print big_intervals, extra

        return changes+extra*2

    def run(self):
        self.results = [self.calculate(c_times, j_times) for c_times, j_times in self.times]

Parenting("B-large (2)")
