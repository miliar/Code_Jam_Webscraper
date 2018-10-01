import sys


class BathroomStalls:

    def __init__(self):
        self.read_file()
        self.resolve_cases()
        self.write_file()

    def read_file(self):
        with open(sys.argv[1]) as fin:
            lines = fin.readlines()[1:]
            lines = [line.replace("\n", "") for line in lines]

        self.lines = lines

    def resolve_cases(self):
        solutions = []
        for line in self.lines:
            solution = self.resolve_case(line)
            solutions.append(solution)

        self.solutions = solutions

    def resolve_case(self, case):
        i = 1
        while len(case) - i > 0:
            right = case[len(case) - i]
            left = case[len(case) - i - 1]
            if left > right:
                case = int(case)
                case = case - (case % (10 ** i) + 1)
                case = str(case)
            i += 1

        return case

    def write_file(self):
        (file_path, extension) = sys.argv[1].split(".")
        file_path = "{}_solved.{}".format(file_path, extension)

        with open(file_path, "w") as fout:
            for case in range(len(self.solutions)):
                fout.write("Case #{}: {}\n".format(case + 1, self.solutions[case]))


if __name__ == "__main__":
    bathrom_stalls = BathroomStalls()
