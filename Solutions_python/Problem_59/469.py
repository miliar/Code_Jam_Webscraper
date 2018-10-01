#!python3

def add_to_tree(tree, path, dir_cache, count=0):
    """Add path (list of directories)
    to the directory tree (dict)."""
    if not path:
        return count
    if path[0] not in tree:
        tree[path[0]] = {}
        count = count + 1
        #print('creating', path[0], ', count =', count)
    return add_to_tree(tree[path[0]], path[1:], dir_cache, count)

def nr_mkdirs(dirs, new):
    root = {}
    dir_cache = {}

    # create tree
    for d in dirs:
        path = list(filter(None, d.split('/')))

        add_to_tree(root, path, dir_cache)

    # make new dirs
    s = 0
    for d in new:
        #print('===', d, '===')
        path = list(filter(None, d.split('/')))
        s += add_to_tree(root, path, dir_cache)

    return s

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    dirs = [input() for _ in range(N)]
    new = [input() for _ in range(M)]
    print('Case #{}: {}'.format(t, nr_mkdirs(dirs, new)))

