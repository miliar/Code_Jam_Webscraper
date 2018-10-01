from collections import defaultdict, namedtuple
from itertools import product

chest = namedtuple('chest', 'needs gives id')

def impossible(chests, keys):
    needed = defaultdict(int)
    total = defaultdict(int)
    for c in chests:
        needed[c.needs] += 1
        for g in c.gives:
            total[g] += 1
    for k in keys:
        total[k] += keys[k]

    for key in needed: #not enough keys of type key
        if needed[key] > total[key]:
            return True

    for c in chests:  # all keys to unlock c are within c
        if total[c.needs] == len([g for g in c.gives if g == c.needs]):
            return True

    return False

def valid(keys, strategy):
    k = keys.copy()

    for s in strategy:
        needed = s.needs
        if k[needed] <= 0:
            return False
        k[needed] -= 1
        for key in s.gives:
            k[key] += 1

    return True


def find_valid(chests, keys, strategy=None, opened=None):
    opened = opened or defaultdict(bool)
    strategy = strategy or []

    unopened = [c for c in chests if not opened[c]]
    if impossible(unopened, keys):
        return None

    def _choose(c):
        keys[c.needs] -= 1
        for k in c.gives:
            keys[k] += 1
        opened[c] = True
        strategy.append(c)

    def _undo(c):
        keys[c.needs] += 1
        for k in c.gives:
            keys[k] -= 1
        opened[c] = False
        strategy.pop()

    def _try(c):
        _choose(c)
        solution = find_valid(chests, keys, strategy, opened)
        if solution is not None:
            return solution
        _undo(c)
        return None

    if len(strategy) == len(chests):
        return strategy

    for c in chests:
        if opened[c] or keys[c.needs] <= 0:
            continue

        result = _try(c)
        if result is not None:
            return result


def tostr(solution):
    if solution is None:
        return 'IMPOSSIBLE'
    return ' '.join(str(s.id) for s in solution)


def test():
    chests = [chest(needs=1, gives=tuple(), id=1),
              chest(needs=1, gives=(1, 3), id=2),
              chest(needs=2, gives=tuple(), id=3),
              chest(needs=3, gives=(1, 2), id=4)]
    keys = defaultdict(int)
    keys[1] = 1

    assert tostr(find_valid(chests, keys)) == '2 1 4 3'

    chests = [chest(needs=1, gives=tuple(), id=1),
              chest(needs=1, gives=tuple(), id=2),
              chest(needs=1, gives=tuple(), id=3)]
    keys = defaultdict(int)
    keys[1] = 3

    assert tostr(find_valid(chests, keys)) == '1 2 3'

    chests = [chest(needs=1, gives=(1,), id=1)]
    keys = defaultdict(int)
    keys[2] = 1

    assert tostr(find_valid(chests, keys)) == 'IMPOSSIBLE'

    print 'Tests pass'


def main(fname):
    data = [d.strip() for d in open(fname + '.in')]
    out = open(fname + '.out', 'w')

    T = int(data[0])
    data = data[1:]

    for i in range(1, T + 1):

        nkey, nchest = map(int, data[0].split())
        keys = defaultdict(int)
        for key in data[1].split():
            keys[int(key)] += 1

        chests = []
        for id, d in enumerate(data[2: 2 + nchest], 1):
            nums = map(int, d.split())
            c = chest(needs=nums[0], gives=tuple(nums[2:]), id=id)
            chests.append(c)

        if impossible(chests, keys.copy()):
            result = 'IMPOSSIBLE'
        else:
            result = find_valid(chests, keys.copy())
            if result:
                assert valid(keys, result)
            result = tostr(result)

        print 'Case #%i: %s' % (i, result)
        out.write('Case #%i: %s\n' % (i, result))

        data = data[nchest + 2:]

    out.close()


if __name__ == "__main__":
    test()
    import sys
    main(sys.argv[1])
