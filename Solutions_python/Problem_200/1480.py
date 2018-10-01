T = int(input())

for t in range(1,T+1):
    N = int(input())
    if N < 10:
        print("Case #{:d}: {:d}".format(t, N))
        continue
    digits = list(str(N))
    pairs = zip(digits, digits[1:])
    idx = -1
    equal_start=0
    equal_end=0
    repeating_digit = digits[0]
    for i,(d1,d2) in enumerate(pairs):
        if d1 == d2:
            equal_end += 1
        elif d1 > d2:
            idx = i
            break
        else:
            equal_start = i+1
            equal_end = i+1
            repeating_digit = digits[i+1]
    if idx == -1:
        print("Case #{:d}: {:d}".format(t, N))
    else:
        if digits[idx] == repeating_digit and equal_end == idx:
            idx = equal_start
        digits[idx] = chr(ord(digits[i]) - 1)
        digits[idx+1:] = [ '9' for _ in range(idx+1,len(digits)) ]
        print('Case #{:d}: {:d}'.format(t, int(''.join(digits))))
