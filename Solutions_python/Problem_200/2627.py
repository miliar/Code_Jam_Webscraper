# receives a list of digits as input and outputs the tidy number associated
def tidy_up(n):
    d_len = len(n)
    if d_len == 1:
        return int(n[0])
    first_untidy = 0
    tidy = True
    for pos, digit in enumerate(n[1:], 1):
        if digit < n[pos-1]:
            tidy = False
            break
        elif digit > n[pos - 1]:
            first_untidy = pos
    # correct digits from the first untidy until the end
    if not tidy:
        n[first_untidy] -= 1
        index = first_untidy + 1
        while index < d_len:
            n[index] = 9
            index += 1
    return int(''.join(str(i) for i in n))

t = int(input())
for i in range(1, t+1):
    k = [ int(n) for n in input()]
    number = tidy_up(k)
    print("Case #{}: {}".format(i, number))
