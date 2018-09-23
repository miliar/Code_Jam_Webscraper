from solution import Solution
import numpy as np

COLOR_DICT = {"R": ["R"],
              "Y": ["Y"],
              "B": ["B"],
              "O": ["R", "Y"],
              "G": ["Y", "B"],
              "V": ["R", "B"]}

COLOR_DICT = {"R": ["R"],
              "Y": ["Y"],
              "B": ["B"],
              "O": ["R", "Y"],
              "G": ["Y", "B"],
              "V": ["R", "B"]}


BASE = ["R", "Y", "B"]
MIXED = ["RGR", "YVY", "BOB"]


def get_sequence(sequence, mixed_counts):
    str_sequence = []
    print sequence
    for c in sequence:
        if mixed_counts[c] > 0:
            str_sequence.append(MIXED[c])
            mixed_counts[c] -= 1
        else:
            str_sequence.append(BASE[c])
    return "".join(str_sequence)


def from_counts(counts):
    idxs = np.argsort(counts)
    n_pairs = counts[idxs[1]]-counts[idxs[0]]
    n_alternating = counts[idxs[2]] - n_pairs - counts[idxs[0]]
    n_triplets = counts[idxs[2]]-n_pairs-2*n_alternating
    print n_pairs, n_triplets
    triplets = n_triplets*list(idxs[::-1])
    alternating = n_alternating*[idxs[2], idxs[1], idxs[2], idxs[0]]
    pairs = n_pairs*list(idxs[:0:-1])
    return triplets+alternating + pairs


def find_sequence(counts):
    print counts

    base_counts = np.array([counts[0], counts[2],
                            counts[4]], dtype="int")
    mix_counts = np.array([counts[3], counts[5],
                           counts[1]], dtype="int")
    print mix_counts
    print base_counts

    if any(mix_counts > base_counts):
        print "MORE MIX"
        return "IMPOSSIBLE"

    combined_counts = base_counts-mix_counts
    print combined_counts
    for i in range(len(base_counts)):
        if base_counts[i] > 0 and mix_counts[i] == base_counts[i]:
            for j in range(len(base_counts)):
                if j != i and (base_counts[j] or mix_counts[j]):
                    print "CIRCLE"
                    return "IMPOSSIBLE"
            cs = BASE[i] + MIXED[i][1]
            print cs
            return base_counts[i]*cs

    m = sum(combined_counts)/2
    if any(combined_counts > m):
        return "IMPOSSIBLE"

    sequence = from_counts(combined_counts)
    a = get_sequence(sequence, mix_counts)
    print a
    return a


class StableNeighbours(Solution):
    def parse_line(self, line):
        return [int(c) for c in line.split()][1:]

    def calculate(self, d, horses):
        times = []
        for k, s in horses:
            remain = d-k
            times.append(float(remain)/s)
        maxtime = max(times)
        if maxtime == 0:
            assert d == 0, (d, horses)
            return 0
        return float(d)/maxtime

    def run(self):
        self.results = [find_sequence(i) for i in self.inputs]


StableNeighbours("B-small-attempt0")
