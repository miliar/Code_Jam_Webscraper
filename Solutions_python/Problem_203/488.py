t = int(input())

for c in range(1, t+1):
    numbers = [int(n) for n in input().split()]
    row = numbers[0]
    col = numbers[1]
    cake = []
    nonempty = []
    for r in range(row):
        row = input()
        for cell in row:
            if cell != '?':
                nonempty.append(r)
                break
        cake.append(row)
    # for row in cake:
    #     print(row)
    # print(nonempty)
    for row in nonempty:
        last = 0
        fill_head = True
        if cake[row][0] == '?':
            fill_head = True
        else:
            fill_head = False
        for index, cell in enumerate(cake[row]):

            if cell != '?':
                if fill_head:
                    fill_head = False
                    cake[row] = cell * index + cake[row][index:]
                tocopy = index + 1
                while tocopy < len(cake[row]) and cake[row][tocopy] == '?':
                    tocopy += 1
                tocopy -= 1
                cake[row] = cake[row][0:index+1] + cell *(tocopy-index) + cake[row][tocopy+1:]
                last = index
    for index,row in enumerate(cake):
        if nonempty.count(index) == 0:
            tocopy1 = index + 1
            if tocopy1 >= len(cake):
                tocopy1 = len(cake) - 1
            tocopy2 = index - 1
            if tocopy2 < 0:
                tocopy2 = 0
            while nonempty.count(tocopy2) == 0 and nonempty.count(tocopy1) == 0:
                tocopy1 += 1
                if tocopy1 >= len(cake):
                    tocopy1 = len(cake) - 1
                tocopy2 -= 1
                if tocopy2 < 0:
                    tocopy2 = 0
            if nonempty.count(tocopy2) == 0:
                cake[index] = cake[tocopy1]
            else:
                cake[index] = cake[tocopy2]
    print('Case #{0}:'.format(c))
    for row in cake:
        print(row)
