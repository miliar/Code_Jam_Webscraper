import sys

def get_ith(ls, i):
    return map(lambda l: l[i] if i < len(l) else None, ls)

def count(create_file, existing_files):
    res = 0

    for i in xrange(len(create_file)):
        prefix = create_file[:len(create_file) - i]

        for existing in existing_files:
            curr = existing[:len(prefix)]
            if prefix == curr:
                return len(create_file) - len(prefix)

    return len(create_file)

def solve(existing_files, create_files):
    res = 0

    for create_file in create_files:
        res += count(create_file, existing_files)
        existing_files.append(create_file)

    return res

T = int(raw_input())

for t in xrange(T):
    N, M = map(int, sys.stdin.readline().split(' '))

    existing_files = [sys.stdin.readline().strip('\n') for i in xrange(N)]
    create_files = [sys.stdin.readline().strip('\n') for i in xrange(M)]

    existing_files = map(lambda f: filter(None, f.split('/')), existing_files)
    create_files = map(lambda f: filter(None, f.split('/')), create_files)

    print 'Case #%d: %d' % (t+1, solve(existing_files, create_files))
