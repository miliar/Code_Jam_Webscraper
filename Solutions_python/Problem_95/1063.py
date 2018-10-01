
def translate(s,mapping):
    s2 = [mapping[i] for i in s]
    return "".join(s2)


mapping = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i',
        'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w',
        'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

n = int(raw_input())

for i in range(1,n+1):
    s = raw_input()
    print 'Case #{}: {}'.format(i,translate(s,mapping))
