mapping = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}

mapping['z'] = 'q'
mapping['q'] = 'z'
mapping[' '] = ' '

with open("output.out", "w") as f2:
    with open("A-small.in") as f:
        n = int(f.readline())
        for i in range(n):
            inp = f.readline()[:-1]

            print("Case #", i+1, ": ", "".join(map(lambda x: mapping[x], inp)), sep="", file=f2)
