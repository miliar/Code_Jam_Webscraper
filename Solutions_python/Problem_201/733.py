# problem 1
import sys
sys.path.append('/Users/jakemagner/Desktop/google_code_jam/year_2017/')

from util.io import get_only_file_in_downloads


_times_called = 0
_args_set = set()


def get_or_none(gen):
    try:
        return gen.next()
    except StopIteration:
        return None


def reset():
    global _times_called
    global _args_set
    _times_called = 0
    _args_set = set()


def view():
    print 'Times Called: %d' % _times_called
    print 'Unique Args: %d' % len(_args_set)


def ifunc(N):
    """ Yields, the min, max, and times in a row
    ifunc(5)
        (2, 2, 1)
        (0, 1, 2)
        (0, 0, 2)
    """
    global _times_called
    global _args_set
    _args_set.add(N)
    _times_called += 1
    if N == 1:
        yield (0, 0, 1)
        raise StopIteration()
    if N == 2:
        yield (0, 1, 1)
        yield (0, 0, 1)
        raise StopIteration()
    if N % 2 != 0:  # odd
        half = (N - 1) / 2
        yield (half, half, 1)
        for res in ifunc(half):
            yield (res[0], res[1], res[2] * 2)
        raise StopIteration()
    yield (N - 2) / 2, N / 2, 1
    left_side_N = (N - 2) / 2
    right_side_N = (N / 2)
    left_side_gen = ifunc(left_side_N)
    right_side_gen = ifunc(right_side_N)
    next_left = left_side_gen.next()
    next_right = right_side_gen.next()
    while next_left and next_right:
        if next_right is None or next_left[0] > next_right[0] or (next_left[0] == next_right[0] and next_left[1] > next_right[1]):
            yield next_left
            pull_from = 'left'
        elif next_left is None or next_right[0] > next_left[0] or (next_left[0] == next_right[0] and next_right[1] > next_left[1]):
            yield next_right
            pull_from = 'right'
        elif next_right[0] == next_left[0] and next_right[1] == next_left[1]:
            yield next_left[0], next_left[1], next_left[2] + next_right[2]
            pull_from = 'both'
        if pull_from in ('left', 'both'):
            next_left = get_or_none(left_side_gen)
        if pull_from in ('right', 'both'):
            next_right = get_or_none(right_side_gen)
    raise StopIteration


_ifunc_cache = {}


def ifunc_list(N):
    """ Returns, the min, max, and times in a row when you start with N stalls
    ifunc(5)
        (2, 2, 1)
        (0, 1, 2)
        (0, 0, 2)
    """
    global _ifunc_cache
    if N in _ifunc_cache:
        return _ifunc_cache[N]
    global _times_called
    global _args_set
    _args_set.add(N)
    _times_called += 1
    if N == 1:
        return [(0, 0, 1)]
    if N == 2:
        return [(0, 1, 1), (0, 0, 1)]
    if N % 2 != 0:  # odd
        half = (N - 1) / 2
        result = []
        result.append((half, half, 1))
        for res in ifunc_list(half):
            result.append((res[0], res[1], res[2] * 2))
        _ifunc_cache[N] = result
        return result
    result = []
    result.append(((N - 2) / 2, N / 2, 1))
    left_side_N = (N - 2) / 2
    right_side_N = (N / 2)
    left_side = ifunc_list(left_side_N)
    right_side = ifunc_list(right_side_N)
    next_left_ind = 0
    next_right_ind = 0
    next_left = left_side[next_left_ind]
    next_right = right_side[next_right_ind]
    while next_left and next_right:
        if next_right is None or next_left[0] > next_right[0] or (next_left[0] == next_right[0] and next_left[1] > next_right[1]):
            result.append(next_left)
            pull_from = 'left'
        elif next_left is None or next_right[0] > next_left[0] or (next_left[0] == next_right[0] and next_right[1] > next_left[1]):
            result.append(next_right)
            pull_from = 'right'
        elif next_right[0] == next_left[0] and next_right[1] == next_left[1]:
            result.append((next_left[0], next_left[1], next_left[2] + next_right[2]))
            pull_from = 'both'
        if pull_from in ('left', 'both'):
            next_left_ind += 1
            if len(left_side) > next_left_ind:
                next_left = left_side[next_left_ind]
            else:
                next_left = None
        if pull_from in ('right', 'both'):
            next_right_ind += 1
            if len(right_side) > next_right_ind:
                next_right = right_side[next_right_ind]
            else:
                next_right = None
    _ifunc_cache[N] = result
    return result


def solve_stalls(N, K):
    for min_space, max_space, num_times in ifunc_list(N):
        K -= num_times
        if K <= 0:
            return (max_space, min_space)


def generate_output(input_file):
    num_cases = None
    for i, line in enumerate(input_file):
        if i == 0:
            num_cases = int(line.strip())
            continue
        if i > num_cases:
            break
        N, K = line.split()
        N = int(N.strip())
        K = int(K.strip())
        max_, min_ = solve_stalls(N, K)
        print 'Case #%d: %d %d' % (i, max_, min_)


if __name__ == '__main__':
    path = None
    if len(sys.argv) == 2:
        path = sys.argv[1]
    if path is None:
        input_file = get_only_file_in_downloads()
    else:
        input_file = open(path)
    generate_output(input_file)
