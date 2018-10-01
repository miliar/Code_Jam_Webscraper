mapping = {"R": 0, "Y": 1, "B": 2}

with open("B-small-attempt2.in") as f:
    with open("output.txt", "w") as g:
        t = int(f.readline().strip())
        for i in range(1, t + 1):
            print(i)
            [n, r, o, y, gr, b, v] = map(int, f.readline().split())

            for j in [r, y, b]:
                if 2 * j > sum([r, y, b]):
                    g.write("Case #{}: IMPOSSIBLE\n".format(i))
                    break
            else:
                # a solution exists
                sol = []
                if r > y:
                    if r > b:
                        most = "R"
                        rest = ["B", "Y"]
                    else:
                        most = "B"
                        rest = ["R", "Y"]
                else:
                    if y > b:
                        most = "Y"
                        rest = ["R", "B"]
                    else:
                        most = "B"
                        rest = ["R", "Y"]

                arr = [r, y, b]
                while arr[mapping[most]] > 0:
                    sol.append(most)
                    arr[mapping[most]] -= 1
                    if arr[mapping[rest[0]]] > arr[mapping[rest[1]]]:
                        sol.append(rest[0])
                        arr[mapping[rest[0]]] -= 1
                    else:
                        sol.append(rest[1])
                        arr[mapping[rest[1]]] -= 1
                while sum(arr) > 0:
                    if arr[mapping[rest[0]]] > arr[mapping[rest[1]]]:
                        sol.append(rest[0])
                        arr[mapping[rest[0]]] -= 1
                    else:
                        sol.append(rest[1])
                        arr[mapping[rest[1]]] -= 1

                g.write("Case #{}: {}\n".format(i, "".join(sol)))
