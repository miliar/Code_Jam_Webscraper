# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

# Small Input
'''
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())
    tmp = n
    while True:
        tidy = True
        list_n = [int(i) for i in str(tmp)]
        for x, y in zip(list_n, list_n[1:]):
            # print x, y
            if x > y:
                # print "Not tidy"
                tmp -= 1
                tidy = False
                continue
            else:
                pass
        if tidy:
            print tmp
            break
'''

# Large Input
t = int(raw_input())  # read a line with a single integer
result = []
for i in xrange(1, t + 1):
    n = int(raw_input())
    tmp = n
    while True:
        tidy = True
        # print tmp
        list_n = [int(i) for i in str(tmp)]
        for i in xrange(len(list_n)-1):
            # print x, y
            if list_n[i] > list_n[i+1]:
                # print "Not tidy"
                if list_n[i] == 1 and i == 0:  # Leading 1
                    list_n = [9 for x in xrange(len(list_n)-1)]
                    tmp = ''.join(map(str, list_n))
                    break

                list_n[i] -= 1
                list_n = list_n[:i+1] + [9 for x in xrange(len(list_n)-(i+1))]
                tmp = ''.join(map(str, list_n))
                tidy = False
                continue
            else:
                pass
        if tidy:
            result.append(tmp)
            break

with open("/Users/chenghsi/chchao/misc/google_codejam/long_output", "w") as f:
    for i in xrange(1, t+1):
        f.write("Case #{}: {}\n".format(i, result[i-1]))
