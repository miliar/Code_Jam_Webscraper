def a (fname):
    fin = open(fname + ".in")
    lines = fin.readlines()
    T = int(lines[0])
    fout = open(fname + ".out", "w")
    for t in range(1, T+1):
        line = lines[t].split(" ")
        s_max = int(line[0])
        ns = line[1]
        fout.write("Case #" + str(t) + ": " + str(how_many_friends(s_max, ns)) + "\n")


def how_many_friends(s_max, ns):
    standers = 0
    friends = 0
    for s in range(s_max+1):
        if int(ns[s])>0:
            new_friends = max(s - standers,0)
            friends = friends + new_friends
            standers = standers + new_friends + int(ns[s])
    return friends


