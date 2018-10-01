def flood(cake, x, y, letter):
    if x < 0 or y < 0:
        return
    if cake[x][y] != "?":
        return
    cake[x][y] = letter
    flood(cake, x-1, y, letter)
    flood(cake, x, y-1, letter)

n = int(input())

for i in range(n):
    s = input().split(" ")
    r = int(s[0])
    c = int(s[1])
    cake = []
    for j in range(r):
        cake.append(list(input()))

    for x in range(r):
        last = None
        for y in range(c):
            if cake[x][y] == "?":
                continue
            flood(cake, x-1, y, cake[x][y])
            flood(cake, x, y-1, cake[x][y])
            last = cake[x][y]
        if last:
            flood(cake, x, c-1, last)

    for y in range(c):
        x=r-1
        while cake[x][y] == "?":
            x -= 1
        flood(cake, r-1, y, cake[x][y])
    
    print("Case #{}:".format(i+1))
    print("\n".join([''.join(x) for x in cake]))    
