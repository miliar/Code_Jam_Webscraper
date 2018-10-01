from decimal import Decimal

def next_line(f):
    line = f.readline()
    if line[-1] == '\n':
        line = line[:-1]
    return Decimal(line)


def is_tidy(number):
    number_str = str(number)
    for i in range(1, len(number_str)):
        if number_str[i] < number_str[i-1]:
            return False
    return True

FILE = 'input/B-large.in'

with open(FILE, 'r') as f:
    n_cases = next_line(f)
    for case in range(1, n_cases+1):
        current = next_line(f)
        reversed = str(current)[::-1]
        i = 0
        while i < len(reversed):
            if is_tidy(current):
                print("Case #%d: %d" % (case, current))
                break
            else:
                digit = int(reversed[i])
                aux = (1 + digit) * pow(10, i)
                current = current - aux
                reversed = str(current)[::-1]
                if is_tidy(current):
                    print("Case #%d: %d" % (case, current))
                    break
                i += 1


