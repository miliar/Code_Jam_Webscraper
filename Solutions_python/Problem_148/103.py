from doctest import testmod

def largest_less_than(lst, n, a = None, b = None):
    """Returns the largest element in LST[A:B] that is less than
    or equal to N.

    >>> lst = [1, 2, 3, 4, 5]
    >>> largest_less_than(lst, 3.5)
    3
    """
    if a is None:
        a, b = 0, len(lst)
    print a, b

    if a > b:
        return None
    if a == b and lst[a] > n:
        return None

    mid = (a + b) / 2
    if lst[mid] < n:
        return largest_less_than(lst, n, mid + 1, b)
    elif lst[mid] == n:
        return n
    else: #lst[mid] > n
        return largest_less_than(lst, n, a, mid)

def largest_less_than(lst, n):
    largest = None
    for elt in lst:
        if elt <= n:
            largest = elt
    return largest

def min_disks(files, disk_size):
    """Returns the minimum number of disks needed to fit FILES
    on disks of size DISK_SIZE.

    >>> min_disks([10, 20, 70], 100)
    2
    >>> min_disks([30, 40, 60, 70], 100)
    2
    >>> min_disks([10, 20, 30, 40, 60], 100)
    3
    """
    files = sorted(files)
    disks = 0
    while len(files) > 0:
        file1 = files.pop(0)
        if len(files) > 0:
            file2 = largest_less_than(files, disk_size - file1)
            if file2 is not None:
                files.remove(file2)
        disks += 1

    return disks

def main():
    with open(IN_FILE) as f:
        cases = int(f.readline()[:-1])
        for case in range(cases):
            _, X = [int(x) for x in f.readline()[:-1].split()]
            files = [int(x) for x in f.readline()[:-1].split()]
            print "Case #%s: %s" % (case + 1, min_disks(files, X))

IN_FILE = 'test.in'
OUT_FILE = 'solution.out'

if __name__ == '__main__':
    main()
