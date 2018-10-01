import fileinput

def TidyNumbers(last_num):
    if is_tidy(last_num):
        return int(last_num)

    n = list(reversed(last_num))
    for i in range(len(n) - 1):
        if n[i] < n[i+1]:
            n[i+1] = str(int(n[i+1]) - 1)
            for j in range(i+1):
                n[j] = '9'

    return int(''.join(reversed(n)))

def is_tidy(num):
    snum = ''.join(sorted(num))
    return num == snum

if __name__ == '__main__':
    with fileinput.input() as f:
        n = next(f)
        for i, line in enumerate(f, start=1):
            last_num = line.split()[0]
            result = TidyNumbers(last_num)

            print('Case #{}: {}'.format(i, result))
