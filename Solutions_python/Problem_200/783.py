ret = []
with open('B-large.in', 'r') as file:
    t = int(file.readline())
    for __ in range(t):
        n = int(file.readline())
        x = [int(x) for x in str(n)]
        last = x[-1]
        for i in reversed(range(len(x))):
            if last < x[i]:
                x[i] -= 1
                for j in range(i+1, len(x)):
                    x[j] = 9
            last = x[i]
        ret.append(int(''.join(map(str, x))))


with open('Bout_large.txt', 'w') as outfile:
    for i in range(t):
        outfile.write("Case #%d: %s\n" %(i+1, ret[i]))
