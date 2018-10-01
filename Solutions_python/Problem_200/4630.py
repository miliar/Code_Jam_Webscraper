def determine_tidy_number(x):
    for i in range(x, 0, -1):
        a = 0
        ja = 1
        for j in str(i):
            if int(j) < a:
                ja = 0
                break
            a = int(j)
        if ja:
            return i


def is_decreasing(x):
    a = 9
    for i in str(x):
        if int(i) > a:
            return False
        a = int(i)
    if str(x).count(str(a)) == len(str(x)):
        return False
    return True

n = int(input())
for i in range(n):
    a = int(input())
    if is_decreasing(a) and len(str(a)) != 1:
        a = str(a)
        x = str(int(a[0]) - 1)
        for j in range(1, len(a)):
            x += "9"
    else:
        x = determine_tidy_number(a)
    print("Case #{}:".format(i + 1), int(x))
