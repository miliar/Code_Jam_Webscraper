def main():
    ans = []
    with open("A-large.in", "r") as r:
        count = int(r.readline()[:-1])
        for i in range(count):
            l = r.readline()[:-1]
            cakes, size = l.split(" ")
            lc = len(cakes)
            size = int(size)
            cakes = list(cakes)
            flip = 0
            j = 0
            while j < lc -size +1:
                if cakes[j] == "-":
                    for k in range(j, j+size):
                        if cakes[k] == "-":
                            cakes[k] = "+"
                        else:
                            cakes[k] = "-"
                    flip += 1
                # print(cakes)
                j += 1 
            if "-" in cakes:
                ans.append(-1)
            else:
                ans.append(flip)
    with open("test.out", "w") as w:
        for i, a in enumerate(ans):
            if a >= 0:
                w.write("Case #{0}: {1}\n".format(i+1, a))
            else:
                w.write("Case #{0}: IMPOSSIBLE\n".format(i+1))

if __name__ == '__main__':
    main()