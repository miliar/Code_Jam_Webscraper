input_file = open('/Users/arisha/Desktop/programming/Python/codejam/2013/osmos/A-small-attempt2.in')
output_file = open('/Users/arisha/Desktop/programming/Python/codejam/2013/osmos/A-small.out', 'w')

T = int(input_file.readline())
debug = True

for i in range(T):
    a, n = map(int, input_file.readline().strip().split())
    motes = map(int, input_file.readline().strip().split())
    if debug:
        print a, n
    motes_sorted = motes[:]
    motes_sorted.sort()
    if debug: print motes_sorted
    total = a
    count = 0
    for mote in motes_sorted:
        if mote < total:
            total += mote
        else:
            new_mote = total - 1
            if total + new_mote > mote:
                total += new_mote + mote
                count += 1
                if debug: print "+%d" % new_mote
            else:
                if debug: print "-%d" % mote
                count += 1 #mote deleted
    ans = "Case #%d: %d\n" % (i+1, count)
    if debug: print ans
    output_file.write(ans)

input_file.close()
output_file.close()
