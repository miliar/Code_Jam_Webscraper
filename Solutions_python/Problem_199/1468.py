from solution import Solution
import numpy as np


class PancakeStack(object):
    def __init__(self, pancakes, k=1):
        self.pancakes = np.array(pancakes, dtype="bool")
        self.k = k
        self.result = self.get_n_flips()

    @classmethod
    def from_string(cls, s):
        return PancakeStack([c == "+" for c in s])

    def flip(self, n):
        self.pancakes[:n] = True-self.pancakes[n:0:-1]

    def set_happyface_up(self):
        while not np.all(self.pancakes):
            pass

    def get_n_flips(self):
        n_flips = 0
        for i in range(len(self.pancakes)-self.k+1):
            if not self.pancakes[i]:
                self.k_flip(i)
                n_flips += 1
        if all(self.pancakes):
            return str(n_flips)
        else:
            return "IMPOSSIBLE"

    def k_flip(self, i):
        self.pancakes[i:i+self.k] = np.logical_not(self.pancakes[i:i+self.k])

    def __str__(self):
        return self.result


class Pancakes(Solution):
    def parse_input(self):
        with open(self.input_file) as f:
            f.readline()
            self.inputs = [
                ([c == "+" for c in line.split()[0].strip()+"+"],
                 int(line.split()[1].strip()))
                for line in f.readlines()]

    def run(self):
        self.results = [str(PancakeStack(array, k))
                        for array, k in self.inputs]


Pancakes("A-large")
