f = open("A-large.in")
line = []
for l in f:
    line.append(l.strip())
c = 0
for i in line[1:]:
    c += 1
    data = i.split()
    pan = data[0]
    pan_num = int(data[1])
    r = 0
    impossible = False
    for j in range(len(pan)):
##        print(pan)
##        print(j)
        if pan[j] == '-':
            r += 1
            if j > len(pan) - pan_num:
                print("Case #{}: IMPOSSIBLE".format(c))
                impossible = True
                break
            else:
                new_pan = ''
                for k in range(len(pan)):
                    if k < j or k >= j + pan_num:
                        new_pan += pan[k]
                    else:
                        if pan[k] == '+':
                            new_pan += '-'
                        else:
                            new_pan += '+'
                pan = new_pan
    if not impossible:
        print("Case #{}: {}".format(c, r))

            
