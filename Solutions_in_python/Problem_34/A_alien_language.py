import re

with open('A-large.in') as file :
    L, D, N = map(int, file.readline().split())
    words = [file.readline() for i in range(D)]

    for i in range(N) :
        s = file.readline()
        s = s.replace('(', '[').replace(')', ']')
        count = 0
        for word in words :
            if re.match(s, word) :
                count += 1
        print("Case #{}: {}".format(i + 1, count))
