with open("A-small-attempt0.in") as f:
    lines = f.readlines()

lineno = 0
def readline():
    global lineno
    lineno += 1
    return lines[lineno-1]

cases = int(readline())
for case in range(1, cases+1):
    print("Case #"+str(case)+": ", end="")
    row1 = readline()[:-1]
    r1 = [token for token in row1.split(" ")]
    set1 = [int(token) for token in str(r1[1])]
    agg = 0
    friend = 0
    for value in set1:
        agg += value
        if agg == 0:
            friend += 1
            agg += 1
        agg -= 1
    print(friend)

        
