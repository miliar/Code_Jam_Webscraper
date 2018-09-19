def stripped_lines(lines):
    return (line.rstrip('\n') for line in lines)


def ints(s):
    return [int(num) for num in s.split()]


class memoize(dict):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.func(*key)
        return result
