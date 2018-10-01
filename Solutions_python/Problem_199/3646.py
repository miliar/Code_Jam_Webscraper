import sys
with open(sys.argv[1]) as file:
    next(file)
    counter = 0
    for line in file:
        counter += 1
        pancakes , flipper = line.split( )
        pancakes = list(pancakes)
        flipper = int(flipper)
        flips = 0
        if '-' not in pancakes:
            print "Case #" + str(counter).strip() + ": " + "0"
        else:
            position = 1
            length = len(pancakes)
            for i in xrange(0, length):
                if pancakes[i] is "-":
                    flips += 1
                    if i + flipper <= length:
                        for j in xrange(i, i + flipper):
                            if pancakes[j] is "+":
                                pancakes[j] = "-"
                            else:
                                pancakes[j] = "+"
                    else:
                        for j in xrange(length - flipper, length):
                            if pancakes[j] is "+":
                                pancakes[j] = "-"
                            else:
                                pancakes[j] = "+"
            if '-' not in pancakes:
                print "Case #" + str(counter).strip() + ": " + str(flips)
            else:
                print "Case #" + str(counter).strip() + ": " + "IMPOSSIBLE"
