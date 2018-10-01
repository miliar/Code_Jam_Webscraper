import case

__author__ = 'dmorgant'

def process(input):
    lines = input.splitlines()
    number = int(lines[0])
    output = ""
    for c in range(1, number + 1):
        tokens = lines[c].split(' ')
        solver = Solver(int(tokens[1]), int(tokens[2]), map(int, tokens[3:]))
        output += case.Case(c, solver).output()

    return output.strip()

class Solver:
    def __init__(self, surprisingResults, targetPoints, scores):
        self.targetPoints = targetPoints
        self.surprisingResults = surprisingResults
        self.scores = scores

    def solve(self):
        total = 0
        for score in self.scores:
            remaining = score - (self.targetPoints * 2)
            if remaining + 2 <= 0:
                continue

            if remaining + 2 >=  self.targetPoints:
                total += 1
                continue

            if self.surprisingResults > 0 and remaining + 4 >= self.targetPoints:
                total += 1
                self.surprisingResults -= 1
                continue
        return total
