class InputReader:

    def read(self, filePath):
        with open(filePath, 'r') as f:
            num_cases = int(f.readline())
            cases = []

            for i in range(num_cases):
                line = f.readline().rstrip()
                sizes = line.split(' ');

                grid = []
                for r in range(int(sizes[0])):
                    column = list(f.readline().rstrip())
                    grid.append(column)

                #print(grid)
                cases.append(grid)
        return cases

