x = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', ' ': ' ', '\n': '\n', 'z': 'q', 'q': 'z'}
with open('A-small-attempt0.in', 'r') as f:
    with open('outA-small-attempt0', 'w') as f1:
        n = int(f.readline())
        c = 1
        for i in f:
            ans = ''.join([x[j] for j in i])
            f1.write("Case #{}: {}".format(c, ans))
            c += 1
            
    
