#!/usr/bin/env python

def furthest(list, names):
    """Returns name that appears furthest in the `list', or
    random one from `names' if it's not in the list at all.
    Also returns position, or None (in the second case).
    
    >>> furthest([1, 2, 3], [1, 2, 3])
    (3, 2)
    >>> furthest([1, 2, 2], [1, 2])
    (2, 1)
    >>> furthest([1, 2, 4], [1, 2, 3, 4])
    (3, None)
    
    """
    found = {}
    for name in names:
        found[name] = None
    for index, item in enumerate(list):
        if found.get(item) is None:
            found[item] = index
    max = 0
    for name, pos in found.items():
        if pos is None:
            return (name, None)
        if pos > max:
            max = pos
    return (list[max], max)

def switches(list, names):
    """
    Calculate the number of switches required according
    to task statement.
    
    >>> switches([1, 2, 3], [1, 2, 3])
    1
    >>> switches([1, 2, 3], [1, 2, 3, 4])
    0
    >>> switches(['Y', 'Y', 'G', 'B', 'G', 'N', 'B', 'N', 'D', 'G'],\
                 ['Y', 'N', 'D', 'B', 'G'])
    1
    >>> switches(['A', 'B', 'B'], ['A', 'B'])
    1
    >>> switches(['A', 'B', 'A'], ['A', 'B'])
    2
    
    """
    n = 0
    while list:
        name, pos = furthest(list, names)
        if pos is None:
            break
        n += 1
        list = list[pos:]
    return n

if __name__ == '__main__':
    from sys import argv
    argv = argv[1:]
    if argv:
        f = open(argv[0])
        for caseno in range(int(f.readline())):
            names = []
            list = []
            for i in range(int(f.readline())):
                names.append(f.readline().strip())
            for i in range(int(f.readline())):
                list.append(f.readline().strip())
            print "Case #%d: %d" % (caseno + 1, switches(list, names))
    else:
        import doctest
        doctest.testmod()
