t = int(input())
outputlist = []
for i in range(t):
    inline = input()
    inline = inline.split()
    r = int(inline[0])
    c = int(inline[1])
    
    cake = []
    for row in range(r):
        initial = input()
        if row == 0:
            if initial != ('?'*c):
                startidx = 0
                for inlength in range(len(initial)):
                    if initial[inlength] != '?':
                         if startidx == 0:
                            initial = initial[0:startidx] + initial[inlength]*(inlength-startidx) + initial[inlength:len(initial)]
                            startidx = inlength + 1
                    else:
                        if startidx!=0:
                            initial = initial[0:inlength] + initial[inlength-1] + initial[inlength+1:]
        else:
            if initial == ('?'*c):
                initial = cake[row-1]
            else:
                startidx = 0
                for inlength in range(len(initial)):
                    if initial[inlength] != '?':
                         if startidx == 0:
                            initial = initial[0:startidx] + initial[inlength]*(inlength-startidx) + initial[inlength:len(initial)]
                            startidx = inlength + 1
                    else:
                        if startidx!=0:
                            initial = initial[0:inlength] + initial[inlength-1] + initial[inlength+1:]

        cake.append(initial)

    for row in range(r):
        if cake[row] != ('?'*c):
            for j in range(row):
                cake[j] = cake[row]
            break

    outputlist.append(cake)

for i in range(t):
    print('Case #' + str(i+1) + ':')
    for j in range(len(outputlist[i])):
        print(outputlist[i][j])
