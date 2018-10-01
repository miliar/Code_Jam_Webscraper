def is_tidy(l):
    prev = '0'
    for d in l[:-1]:
        if d < prev:
            return False
        prev = d
    return True

# print([(n, is_tidy(n)) for n in range(25)])


def solve(n):
    """ n is a list, already base 10! """
    d = len(n)

    increased = False
    for i in range(d-2):   # '\n' character at the end
        if n[i] > n[i+1]:
            for j in range(i+1, d-1):
                n[j] = '9'
            increased = True
            break

    if increased:
        n[i] = str(int(n[i]) - 1)

    if n[0] == '0':
        del n[0]

    #print(''.join(n[:-1]))

    if not is_tidy(n):
        return solve(n)  # Horrible hack ;)

    #print('finished')
    return ''.join(n)


input_name = "B-large"
out = open(input_name + ".out", "w")

with open(input_name + ".in", "r") as f:
    lines = f.readlines()
    print(lines)

    t = int(lines[0])

    for i in range(1, t+1):
        out.write("Case #%d: %s" % (i, solve(list(lines[i]))))