from collections import defaultdict
from itertools import combinations

def read_input(path):
    with open(path) as f:
        i = 1
        for line in f.readlines()[2::2]:
            numbers = map(int, line.replace("\n", "").split(" "))

            print i, numbers,
            i += 1
            pancakes = [0] * (max(numbers) + 1)
            for number in numbers:
                pancakes[number] += 1

            yield pancakes

def combine(a, b):
    return (
        max(a[0] + b[1], b[0] + a[1]),
        a[1] + b[1]
    )

def combine_with_special(a, b):
    new_pair = combine(a, b)
    return (new_pair[0] + 1, new_pair[1] + 1)

def get_valueable(pairs):
    times = {}
    for a in pairs:
        if times.get(a[1]) is None or times[a[1]][0] > a[0]:
            times[a[1]] = a

    # clear same valus
    good_times = times.values()
    for a in times.values():
        for b in times.values():
            if a != b and a[0] <= b[0] and a[1] <= b[1] and b in good_times:
                good_times = (
                    good_times[:good_times.index(b)] +
                    good_times[good_times.index(b)+1:])

    return good_times


def create_lookup():
    best_times = defaultdict(list)

    best_times[1] = [(1, 0)]
    best_times[2] = [(2, 0)]
    best_times[3] = [(3, 0)]

    for x in xrange(4,10):
        best_times[x] = [(x, 0)]
        for y in xrange(1, x):
            z = x - y

            if y > z:
                break

            for a in best_times[y]:
                for b in best_times[z]:
                    best_times[x].append(combine_with_special(a, b))

            best_times[x] = get_valueable(best_times[x])
    return best_times


class Pancake(object):
    def __init__(self, pancakes):
        self.pancakes = pancakes
        self.highest_stack = len(pancakes) - 1

        self.special_minutes = 0
        self.best_time = self.highest_stack
        self.lookup = create_lookup()

    def get_pancake(self):
        pancake = self.highest_stack

        self.pancakes[self.highest_stack] -= 1
        self.update_highest_stack()

        return pancake

    def any_left(self):
        return self.highest_stack != 0

    def update_highest_stack(self):
        if self.pancakes[self.highest_stack]:
            return
        self.highest_stack -= 1
        while self.highest_stack > 0 and self.pancakes[self.highest_stack] == 0:
            self.highest_stack -= 1

    def get_time(self):
        return self.highest_stack + self.special_minutes

    def calculate_best_time(self):
        cake = self.get_pancake()

        times = self.lookup[cake]

        while self.any_left():
            cake_b = self.get_pancake()

            times_b = self.lookup[cake_b]

            times_c = []
            for a in times:
                for b in times_b:
                    times_c.append(combine(a, b))

            times = get_valueable(times_c)

        return min(x[0] for x in times)


path = "B-small-attempt4.in"
output = ""
for case, pancakes in enumerate(read_input(path)):
    solver = Pancake(pancakes)

    a = solver.calculate_best_time()
    print "best: {}".format(a)
    output += "Case #{}: {}\n".format(
        case+1, a)

# Remove the last linebreak
output = output[:-1]
with open(path.replace(".in", ".out"), "w") as f:
    f.write(output)