with open("a.in") as fin:
    with open("b.out", "w") as fout:
        t = int(fin.readline())
        for i in range(t):
            (n, m) = tuple(int(x) for x in fin.readline().split())
            dirs = {""}
            count = 0
            for j in range(n):
                dirs.add(fin.readline().strip())
            for j in range(m):
                path = fin.readline().strip()
                parts = path.split("/")
                for k in range(len(parts), 1, -1):
                    npath = "/".join(parts[0:k])
                    if not npath in dirs:
                        dirs.add(npath)
                        count += 1
            fout.write("Case #" + str(i + 1) + ": " + str(count) + "\n")
                    
