def Solution(label, line):
    [des, horses] = line.split()
    des, horses = int(des), int(horses)
    sec = 0
    for h in xrange(horses):
        pos, speed = f.readline().strip('\n').split()
        sec = max(sec, 1.0*(des-int(pos))/int(speed))


    print "Case #{}: {}".format(label, des/sec)
    return 1

if __name__ == '__main__':
    import sys

    file_name = sys.argv[1]
    with open(file_name) as f:
        line = f.readline()
        for i in xrange(1, int(line)+1):
            line = f.readline().strip('\n')
            out = Solution(i, line)
