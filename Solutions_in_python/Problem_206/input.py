class InputReader:

    def read(self, filePath):
        with open(filePath, 'r') as f:
            num_cases = int(f.readline())
            cases = []

            for i in range(num_cases):
                line = f.readline().rstrip()
                case = line.split(' ')

                horses = []
                horses.append(case)
                for num_horses in range(int(case[1])):
                    horse = f.readline().rstrip().split(' ')
                    horses.append(horse)

                print(horses)
                cases.append(horses)
        return cases

