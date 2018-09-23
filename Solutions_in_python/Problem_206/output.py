class OutputWriter:

    def print(self, cases, filepath):
        with open(filepath, 'w') as f:
            for i in range(len(cases)):
                speed = "{:.6f}".format(cases[i])
                f.write('Case #' + str(i+1) + ': ' + speed + '\n')