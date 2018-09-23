def solve(s, k):
    final = "+" * len(s)

    def allFlips(e):
        def flip(c):
            return '-' if c == '+' else '+'

        return ("".join(flip(e[j]) if (i <= j and j < i + k) else e[j] for j in range(len(e))) for i in range(len(e) - k + 1))

    curr, visited, d = {s}, {s}, 0

    while len(curr) != 0 and final not in visited:
        next = set()
        for e in curr:
            for to in allFlips(e):
                if to not in visited:
                    next.add(to)

        visited.update(next)
        curr = next
        d += 1

    if final in visited: return str(d)
    return "IMPOSSIBLE"

def input(file):
    F = open(file, "r")
    T = int(F.readline())
    for i in range(T):
        s, k = F.readline().split(" ")
        yield i + 1, s, int(k)

#for (i, s, k) in input("Asample.in"):
for (i, s, k) in input("A-small-attempt0.in"):
    print("Case #%d: %s" % (i, solve(s, k)))
