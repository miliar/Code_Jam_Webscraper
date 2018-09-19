def calc():
    fi = open("sample.in", "r")
    fo = open("sample.out", "r")

    m1 = {'a': 'y', 'o': 'e', 'z': 'q'}
    m2 = {'q': 'z', 'e': 'o', 'y': 'a'}

    ti = fi.readlines()
    to = fo.readlines()

    for i in range(len(ti)):
        for j in range(len(ti[i])):
            m1[ti[i][j]] = to[i][j]
            m2[to[i][j]] = ti[i][j]
    return m1, m2