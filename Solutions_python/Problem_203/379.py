for t in range(int(input())):
    print("Case #%d:" % (t+1))    
    r, c = map(int, input().split())
    cake = [list(input()) for x in range(r)]
    for row in cake:
        fill = "?"
        first = True
        for (col, i) in enumerate(row):
            if i == "?":
                row[col] = fill
            else:
                fill = i
                if first:
                    for m in range(col):
                        row[m] = fill
                    first = False

    cake = [''.join(row) for row in cake]
    first = ""
    for row in cake:
        if row[0] != "?":
            first = row
            break
    cake[0] = first
    fill = first
    for (i, row) in enumerate(cake):
        if row[0] != "?":
            fill = row
        print(fill)