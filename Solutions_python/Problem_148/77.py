t = input()
# Use greedy

def num_discs(files, x):
    count = 0
    # Remove largest, remove largest that will fit
    while files:
        largest = files.pop()
        i = len(files) - 1
        while i >= 0:
            if files[i] + largest <= x:
                files = files[:i] + files[i+1:]
                break
            i -= 1
        count += 1
    return count

for case in xrange(1, t+1):
    n, x = map(int, raw_input().split())
    discs = map(int, raw_input().split())
    discs.sort()
    print "Case #%d: %d" % (case, num_discs(discs, x))