def solve(line):
    num = list(line)
    start = 0
    found = False
    for i in range(len(num) - 1):
        if num[i] < num[i + 1]:
            start = i + 1
        if num[i] > num[i + 1]:
            found = True
            break
    if not found:
        return line
    return int(line[0:start] + str(int(line[start]) - 1) + '9' * (len(line) - start - 1))
