N = int(raw_input().strip())

key = "welcome to code jam"

for case in range(N):
    text = raw_input().strip()

    # dynamic programming solution
    # keep track of the # of possibilities to get to position 'x' in the key at position 'y' in the text

    map = [[0 for _ in range(len(key) + 1)]] + [[0] for _ in range(len(text))] # pad with 0 to make the starting case easier
    #import pprint; pprint.pprint(map)
    for x in range(len(key)):
        c = key[x]
        for y in range(len(text)):
            tc = text[y]
            if c == tc and (x == 0 or map[y][x] > 0):
                # 1 + above + above-left
                r = map[y][x+1] + map[y][x]
                if x == 0: r += 1
            else:
                # above
                r = map[y][x+1]
            map[y+1].append(r % 10000)

    ct = 0
    print "Case #%d: %04d" % (case+1, map[-1][-1])
#    print text
#    pprint.pprint(map)
#    print map[-1][-1]
