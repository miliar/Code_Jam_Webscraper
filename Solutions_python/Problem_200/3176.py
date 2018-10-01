import sys

def fix(n):
    if len(n) < 2:
        return n
    else:
        if n[-1] < n[-2]:
            n[-2] -= 1
            return fix(n[:-1]) + [9]
        else:
            return n

def solve(number):
    digits = [ord(c)-48 for c in number]
    m = digits[0]
    tidy_number = [m]
    for i, d in enumerate(digits[1:]):
        if d >= m:
            tidy_number.append(d)
            m = d
        else:
            tidy_number[-1] -= 1
            tidy_number = fix(tidy_number) + [9] * (len(digits)-i-1)
            break
    return "".join([chr(c+48) for c in tidy_number if c !=0])

with open(sys.argv[1]) as fh:
    T = int(next(fh))
    for i, line in enumerate(fh):
        print("Case #{}: {}".format(i+1, solve(line.rstrip())))
