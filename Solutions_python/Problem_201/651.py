def calc(file):
    n, k = map(int, file.readline().split())
    s = "{0:b}".format(k)
    max = n
    count = 0
    for _ in xrange(len(s)-1):
        count = count * 2 + 1
        max = max/2

    min = max-1
    max_count = (n - count) - min*(count+1)
    curr = min
    if k <= max_count + count: curr = max
    max = curr/2
    min = curr - max - 1
    return str(max) + " " + str(min)

def main():
    file = open("input.txt")
    fl_o = open("output.txt", 'w')
    T = int(file.readline())
    for t in range(T):
        ans = calc(file)
        fl_o.write("Case #" + str(t+1) + ": " + str(ans) + "\n")
    fl_o.close()

main()