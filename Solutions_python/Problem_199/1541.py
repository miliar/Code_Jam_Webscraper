def invert(S):
    for s in S:
        if s == "+":
            yield "-"
        else:
            yield "+"


def iterate(S,K, iteration):
    while True:
        while len(S) > 0 and S[0] == "+":
            S=S[1:]

        while len(S) > 0 and S[-1] == ["+"]:
            S=S[:-1]

        if len(S) == 0:
            return str(iteration)

        if len(S) >= K:
            S = list(invert(S[:K]))+list(S[K:])
            iteration+=1
            continue
        else:
            return "IMPOSSIBLE"

with open("A-large.in", 'r') as input:
    lines = input.readlines()
    cases = lines[1:]

with open("output.txt", 'w') as output:
    index = 1
    for case in cases:
        S,K = case.split(" ")
        output.write("Case #{i}: {result}\n".format(i=index, result = iterate(S,int(K),0)))
        index +=1


