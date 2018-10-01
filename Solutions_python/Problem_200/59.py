# def choose(n, k, _cache={}):
#     if (n, k) in _cache:
#         return _cache[n, k]
#     prod = 1
#     nn = n
#     kk = 1
#     for x in xrange(k):
#         prod *= nn
#         prod /= kk
#         kk += 1
#         nn -= 1
#     _cache[n, k] = prod
#     return _cache[n, k]


# def count_stuff(first_digit, digit_count):
#     slots = 9 - first_digit + digit_count - 1
#     return choose(slots, digit_count - 1)


# def solve(string):
#     base = 0
#     for length in xrange(1, len(string)):
#         for d in xrange(1, 10):
#             base += count_stuff(d, length)
#             print "{} numbers of length {} with digit {} -- {} so far".format(count_stuff(d, length), length, d, base)
#     extra = 0
#     print "--------EXTRA-------"
#     for index, sdigit in enumerate(string):
#         length = len(string) - index
#         digit = int(sdigit)
#         for d in xrange(1, digit):
#             extra += count_stuff(d, length)
#             print "{} numbers of length {} with digit {} -- {} so far".format(count_stuff(d, length), length, d, extra)
#     return base + extra

def change(string):
    builder = []
    for index, sd in enumerate(string):
        if index + 1 == len(string):
            builder.append(sd)
        else:
            dig = int(sd)
            ndig = int(string[index + 1])
            if ndig < dig:
                builder.append(str(dig - 1))
                break
            else:
                builder.append(str(dig))
    return ''.join(builder) + '9' * (len(string) - len(builder))


def solve(string):
    prev = string
    curr = change(prev)
    while prev != curr:
        prev = curr
        curr = change(curr)
    return int(curr)

cases = int(raw_input())
for ctr in xrange(cases):
    string = raw_input()
    answer = solve(string)
    print "Case #{}: {}".format(ctr + 1, answer)
