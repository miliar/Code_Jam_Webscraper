

def tidy_number(N):
    n = list(map(int, str(N)))
    i = 0
    while i < len(n) - 1:
        if n[i] > n[i + 1]:
            while i > 0 and n[i] == n[i - 1]:
                i -= 1
            n[i] -= 1
            for j in range(i + 1, len(n)):
                n[j] = 9
            break
        i += 1
    return ''.join(map(str, n)).lstrip('0')


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        print("Case #{}: {}".format(i + 1, tidy_number(N)))
