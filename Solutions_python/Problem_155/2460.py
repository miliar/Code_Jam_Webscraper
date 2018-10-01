t = input()
for case in range(t):
    line = raw_input().split(' ')
    smax = int(line[0])
    audience = line[1]
    total = 0
    additional = 0
    for shyness in range(smax + 1):
        if shyness > total:
            additional += shyness - total
            total = shyness
        total += int(audience[shyness]);
    print 'Case #' + str(case + 1) + ': ' + str(additional);
 
