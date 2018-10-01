import numpy as np

def solve(s, k):
    # s is a numpy array
    flips = 0
    for i in range(len(s) - k + 1):
        if s[i] % 2 == 1:
            s[i:i+k] += 1
            flips += 1
    for i in range(len(s) - k + 1, len(s)):
        if s[i] % 2 == 1:
            return "IMPOSSIBLE"
    return str(flips)

if __name__ == "__main__":
    output = []
    with open('A-large.in') as f:
        inputs = [line.strip() for line in f]
    for i in range(1, len(inputs)):
        s, k = inputs[i].split()
        s = [0 if c is '+' else 1 for c in s]
        k = int(k)
        output.append("Case #%d: " % i + solve(np.array(s), k))

    with open('A_large_output.txt', 'w') as f:
        f.write('\n'.join(output))


'''
# CODE TO TEST MY METHOD

def flip(t):
    return tuple(1-x for x in t)

def generate(l, k):
    tups = {}
    def rec_gen(t):
        if len(t) == l:
            tups[t] = -1
        else:
            rec_gen(t+(0,))
            rec_gen(t+(1,))
    rec_gen(())

    reachable = [((0,)*l, 0)]
    seen = set([reachable[0][0]])
    while reachable:
        new_reachable = []
        for t, flips in reachable:
            for i in range(l - k + 1):
                new = t[:i] + flip(t[i:i+k]) + t[i+k:]
                if new not in seen:
                    seen.add(new)
                    new_reachable.append((new, flips+1))
            tups[t] = flips
        reachable = new_reachable

    return tups

for l in range(1, 13):
    for k in range(1, l+1):
        print(l, k)
        tups = generate(l, k)
        for t, f in tups.items():
            res = solve(np.array(t), k)
            if f == -1:
                assert res == "IMPOSSIBLE"
            else:
                assert res == str(f)
'''