class InputReader:

    def read(self, filePath):
        with open(filePath, 'r') as f:
            num_cases = int(f.readline())
            cases = []

            for i in range(num_cases):
                line = f.readline().rstrip()
                cases.append(line)
        return cases