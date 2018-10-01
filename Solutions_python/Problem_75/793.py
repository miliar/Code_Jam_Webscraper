with open("B-large.in") as fin:
    with open("B.out", "w") as fout:
        T = int(fin.readline())
        for q in range(T):
            args = fin.readline().strip().split(" ")
            C = int(args[0])
            D = int(args[C + 1])
            N = int(args[C + D + 2])
            print(args)
            combos = {}
            opposed = set()
            for s in range(C):
                combos[tuple(sorted(args[s + 1][:2]))] = args[s + 1][2]
            for s in range(D):
                opposed.add(tuple(sorted(args[s + C + 2])))
            invoked = []
            for s in range(N):
                invoked.append(args[C + D + 3][s])
                pair = tuple(sorted(invoked[-2:]))
                if pair in combos:
                    invoked[-2:] = [combos[pair]]
                for p in opposed:
                    if p[0] in invoked and p[1] in invoked:
                        invoked = []
            fout.write("Case #" + str(q + 1) + ": " + str(invoked).replace("'", "") + "\n")
