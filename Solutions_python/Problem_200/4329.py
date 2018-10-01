
def check_num(numlist):
    for index in xrange(0, len(numlist) - 1):
        if numlist[index] > numlist[index + 1]:
            return False

    return True

cases = int(raw_input())

for i in xrange(1, cases + 1):
    number = raw_input()
    numl = [int(d) for d in number]
    while check_num(numl) is False and len(numl) > 1:
        for index in xrange(0, len(numl) - 1):
            if numl[index] > numl[index + 1]:
                numl[index] -= 1
                for index2 in xrange(index + 1, len(numl)):
                    numl[index2] = 9

    output = ''.join([str(d) for d in numl])

    print('Case #{0}: {1}'.format(i, int(output)))
