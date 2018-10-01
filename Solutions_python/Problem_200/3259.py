def result(n):
    n = int(n)
    for i in range(n, 0, -1):
        if tidy(i):
            print(i)
            return i

def tidy(i):
    last = 10
    while i:
        r = i % 10
        if r > last:
            return False
        last = min(r, last)
        i /= 10
    return True

if __name__ == "__main__":
    FILE_NAME = 'B-small-attempt0'
    with open(FILE_NAME + '.in') as f:
        with open(FILE_NAME + '.out', 'w') as w:
            r = f.readlines()

            for i in range(len(r) - 1):
                w.write('Case #%d: %s\n' % (i + 1, result(r[i + 1])))