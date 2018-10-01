import os

def find_common(arr_A, arr_B):
    count = 0
    for n in arr_A:
        if n in arr_B:
            count += 1
            output = n

    if count == 1:
        return output
    elif count == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"


f = open("A-small-attempt0.in", 'r')
n_cases = int(f.readline().strip())

for i in xrange(1, n_cases + 1):
    line_n = int(f.readline().strip())
    for j in xrange(1, 5):
        line = f.readline()
        if j == line_n:
            arr_A = line.split()

    line_n = int(f.readline().strip())
    for j in xrange(1, 5):
        line = f.readline()
        if j == line_n:
            arr_B = line.split()

    print "Case #{0}: {1}".format(i, find_common(arr_A, arr_B))




