def max_tidy(t):
    n = len(t)
    if n == 1:
        return t
    found = False
    for i in range(1, n):
        if int(t[i]) < int(t[i - 1]):
            found = True
            break
    if not found:
        return t
    j = 0
    for j in range(i - 1, -1, -1):
        if j != 0:
            if int(t[j]) - 1 >= int(t[j - 1]):
                break
    ret = t[:j] + str(int(t[j]) - 1) + '9' * (n - j - 1)
    return ret if ret[0] != '0' else ret[1:]

if __name__ == "__main__":
    N = int(input())
    output = ""
    for line in range(1, N + 1):
        T = input()
        output += "Case #" + str(line) + ": " + max_tidy(T) + "\n"
    print(output)
