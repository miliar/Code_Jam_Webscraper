def Solution(label, line):
    imp= 'IMPOSSIBLE'
    [pancakes, size] = line.split()
    size = int(size)
    pancakes = list(pancakes)
    idx = 0
    flip = 0
    cnt = 0
    while idx < len(pancakes):
        if pancakes[idx] == '-':
            cnt += 1
            while flip < size:
                if idx + flip >= len(pancakes):
                    print "Case #{}: {}".format(label, imp)
                    return 1
                pancakes[idx+flip] = '+' if pancakes[idx+flip] == '-' else '-'
                flip += 1
            flip = 0
        idx += 1

    print "Case #{}: {}".format(label, cnt)
    return 1

if __name__ == '__main__':
    import sys

    file_name = sys.argv[1]
    with open(file_name) as f:
        line = f.readline()
        for i in xrange(1, int(line)+1):
            line = f.readline().strip('\n')
            out = Solution(i, line)
