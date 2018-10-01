def clap(shyness):
    sp = 0
    required = 0
    for i in range(len(shyness)):
        rp = int(i)
        p = int(shyness[i])
        if p != 0:
            if sp < rp:
                required += rp - sp
                sp += required + p
            else:
                sp += p
    return required


for i in range(input()):
    a, b = raw_input().split()
    print 'Case #' + str(i+1) + ': ' + str(clap(b))
