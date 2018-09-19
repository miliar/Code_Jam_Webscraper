__author__ = 'dmorgant'

class Case:
    def __init__(self, index, solver):
        self.solver = solver
        self.index = index

    def output(self):
        return "Case #" + str(self.index) + ": " + self.solver.solve() + "\n"