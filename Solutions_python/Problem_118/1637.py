fair_squares = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004, 100000020000001 ]


def isPolyndrom(number):
    str_number = str(number)

    for i in xrange(len(str_number) / 2):
        if str_number[i] != str_number[len(str_number) - i - 1]:
            return False
    return True


def isSquarePolindromic(number):
    return isPolyndrom(number) and isPolyndrom(str(number * number))


def getNextPolyndromic(A):
    digits = len(str(A))

    if digits == 1:
        return A + 1
    elif digits == 2:
        if int(str(A + 1)[0] * 2) > A:
            return int(str(A + 1)[0] * 2)
        else:
            return str(int(str(A)[0]) + 1) * 2
    else:
        pass
        # TODO: translate later
        # precomputed in the different way. Didn't translate into python.
        # more than 2 digits


lines = [line.strip() for line in open('C-large-1.in')]
m = int(lines[0])
out = ''

for case in xrange(1, m + 1):
    A, B = map(int, lines[case].split(" "))
    numbers = 0

    for precomputed in fair_squares:
        if precomputed > B:
            break

        if precomputed >= A:
            numbers += 1

    out += "Case #%d: %d\n" % (case, numbers)

with open('output.txt', 'w') as fd:
    fd.write(out[:-1])