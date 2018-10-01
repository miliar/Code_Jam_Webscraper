lines = open("A-small-attempt0.in").read().split("\n")[1:]
for i in range(len(lines) / 10):
    a = int(lines[i * 10])
    b = int(lines[i * 10 + 5]) + 5
    x = set(lines[i * 10 + a].split(" ")) & set(lines[i * 10 + b].split(" "))
    ans = "Volunteer cheated!"
    if len(x) > 1:
        ans = "Bad magician!"
    elif len(x) == 1:
        ans = list(x)[0]
    print "Case #%d:" % (i+1), ans


