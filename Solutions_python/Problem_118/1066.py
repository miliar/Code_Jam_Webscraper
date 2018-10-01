import sys
import math
import multiprocessing

def is_fair(number):
    n = str(number)
    while len(n) > 1:
        if n[0] != n[-1]:
            return False
        n = n[1:-1]
    return True

def is_square(number):
    n = math.sqrt(number)
    if n.is_integer():
        return is_fair(int(n))
    return False

def solve(start, end):
    count = 0
    for x in range(start, end + 1):
        if is_fair(x) and is_square(x):
            count = count + 1
    return count

def simple_solve(number):
    if is_fair(number) and is_square(number):
        return 1
    return 0

def main():
    try:
        path = sys.argv[1]
        results = []
        count = []
        with open(path, 'r') as f:
            cases = int(f.readline())
            for i in range(cases):
                start, end = f.readline().split(' ')
                start, end = int(start), int(end)
                pool = multiprocessing.Pool()
                count = pool.map(simple_solve, range(start, end + 1))
                results.append("Case #{0}: {1}{2}".format(i + 1, sum(count), '\n' if i < cases - 1 else ''))
        with open(path + '-results', 'w') as fr:
            fr.write(''.join(results))
    except FileNotFoundError:
        print("Couldn't find file!")
    except IndexError:
        print("usage: fair_n_square.py <path_to_file>")

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
