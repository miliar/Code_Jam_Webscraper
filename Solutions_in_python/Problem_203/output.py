class OutputWriter:

    def print(self, cases, filepath):
        with open(filepath, 'w') as f:

            for i in range(len(cases)):
                f.write('Case #' + str(i+1) + ':'+ '\n')
                for row in cases[i]:
                    f.write(''.join(str(j) for j in row)+ '\n')

