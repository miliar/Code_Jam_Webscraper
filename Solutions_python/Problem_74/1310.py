data = open("input01.txt", "r").readlines()
cases = int(data.pop(0))

def run(line):
    sums = {"O" : 0, "B" : 0}
    last = {"O" : 1, "B" : 1}
    tok = line.split(" ")
    count = int(tok.pop(0))
    last_color = None
    for i in range(0, count*2, 2):
        color = tok[i]
        num = int(tok[i+1])
        if last_color and last_color != color:
            if sums[color] + abs(last[color] - num) < sums[last_color]:
                sums[color] = sums[last_color]
            else:
                sums[color] += abs(last[color] - num)
        else:
            sums[color] += abs(last[color] - num)
        last[color] = num
        last_color = color
        sums[color] += 1 # +1 for the actual act of button-pushing

    return max(sums["O"], sums["B"])




for i in range(cases):
    print "Case #%d: %d" % (i+1, run(data[i]))

