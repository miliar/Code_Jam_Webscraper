infile = open('B-small-attempt1.in', 'r')
outfile = open('test.out', 'w')

T = int(infile.readline())


def valid_neighbor(N):
    return list(map(lambda x: x % 6, range(N + 2, N + 5)))


def set_unicorn_string(lst):
    unicorns = ['R', 'O', 'Y', 'G', 'B', 'V']
    res = ''
    for i in lst:
        res += unicorns[i]
    return res


def check_possible(unicorns):
    for i in range(len(unicorns)):
        tmp = 0
        neighbors = valid_neighbor(i)
        for n in neighbors:
            tmp += unicorns[n]
        if unicorns[i] > tmp + 1:
            return False
    return True

for t in range(1, T + 1):
    lst = list(map(int, infile.readline().strip().split()))
    N = lst[0]
    unicorns = lst[1:]
    if not check_possible(unicorns):
        outfile.write('Case #{}: IMPOSSIBLE\n'.format(t))
        continue
    arrangement = []
    for i in range(N - 1):
        sorted_index = [i[0] for i in sorted(enumerate(unicorns), key=lambda x: -x[1])]
        passed = False
        for ind in sorted_index:
            if not arrangement:
                arrangement.append(ind)
                unicorns[ind] -= 1
                passed = True
                break
            else:
                head = arrangement[0]
                tail = arrangement[-1]
                if ind in valid_neighbor(head):
                    arrangement.append(ind)
                    unicorns[ind] -= 1
                    passed = True
                    break
                if ind in valid_neighbor(tail):
                    arrangement.append(ind)
                    unicorns[ind] -= 1
                    passed = True
                    break
        if not passed:
            break

    if arrangement[0] in valid_neighbor(arrangement[-1]):
        success = False
        for i in range(N - 1):
            head = arrangement[i]
            tail = arrangement[(i + 1) % (N - 1)]
            sorted_index = [i[0] for i in sorted(enumerate(unicorns), key=lambda x: -x[1])]
            ind = sorted_index[0]
            if ind in valid_neighbor(head) and ind in valid_neighbor(tail):
                arrangement = arrangement[:i + 1] + [ind] + arrangement[i + 1:]
                res = set_unicorn_string(arrangement)
                success = True
                break
            else:
                continue
        if not success:
            res = 'IMPOSSIBLE'
    else:
        head = arrangement[0]
        tail = arrangement[-1]
        sorted_index = [i[0] for i in sorted(enumerate(unicorns), key=lambda x: -x[1])]
        ind = sorted_index[0]
        if ind in valid_neighbor(head) and ind in valid_neighbor(tail):
            arrangement.append(ind)
            res = set_unicorn_string(arrangement)
            success = True
        else:
            res = 'IMPOSSIBLE'
    outfile.write('Case #{}: {}\n'.format(t, res))
