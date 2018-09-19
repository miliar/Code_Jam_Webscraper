import sys
import copy
from itertools import product

def ordered(seq):
    for i, j in zip(seq, seq[1:]):
        if not (i < j):
            return False
    return True

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    message = "welcome to code jam"

    for case in range(1, N+1):
        line = "".join([c for c in sys.stdin.readline().strip() if c in message])

        line_indices = dict([(i, []) for i in message])
        for i in range(len(line)):
            if line[i] in message:
                line_indices[line[i]].append(i)

        # remove all indices that occur before the first occurrence of the
        # previous letter
        ordered_indices = [copy.deepcopy(line_indices[i]) for i in message]
        min = 0
        for i in range(len(ordered_indices)):
            for j in range(len(ordered_indices[i])):
                if ordered_indices[i][j] >= min:
                    min = ordered_indices[i][j]
                    break
            del ordered_indices[i][:j]

        # remove all indices that occur after the last occurrence of the
        # following letter
        max = 1 + len(line)
        for i in reversed(range(len(ordered_indices))):
            for j in reversed(range(-1, len(ordered_indices[i]))):
                if j < 0:
                    break
                elif ordered_indices[i][j] <= max:
                    max = ordered_indices[i][j]
                    break
            del ordered_indices[i][j+1:]

        permutes = product(*ordered_indices)
        print "Case #{0}: {1:04}".format(case, sum(map(ordered, permutes)) % 10000)
