import sys


class TestCase(object):
    def __init__(self, D, N, horses):
        self.D = D
        self.N = N
        self.horses = horses
        pass

    def _find_max_speed(self, distance, speed):
        time_left_for_horse = (self.D - distance) / float(speed)

        if time_left_for_horse > 0:
            max_speed_for_time = float(self.D) / time_left_for_horse
        else:
            max_speed_for_time = distance

        return max_speed_for_time

    def solve(self):
        max_speeds = [self._find_max_speed(horse[0], horse[1]) for horse in self.horses]

        return min(max_speeds)


def parse(input_file_path):
    test_cases = []

    with open(input_file_path, "r") as input_file:
        test_cases_number = int(input_file.readline())
        for i in xrange(test_cases_number):
            line = input_file.readline()
            D, N = line.split(" ")
            horses = []
            for j in xrange(int(N)):
                line = input_file.readline()
                dist, speed = line.split(" ")
                horses.append((int(dist), int(speed)))

            test_case = TestCase(int(D), int(N), horses)
            test_cases.append(test_case)

    return test_cases


def main(input_file_path):
    test_cases = parse(input_file_path)

    for i, test_case in enumerate(test_cases):
        solution = test_case.solve()
        print "Case #{0}: {1}".format(i+1, solution)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
