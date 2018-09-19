
def translate(inp):
    trans = {'a': 'y', ' ': ' ', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
    out = ""
    for i in inp:
        out += trans[i]
    return out

if __name__ == '__main__':
    try:
        input()
        i = 1
        while True:
            inp = input()
            print("Case #{0}: {1}".format(i, translate(inp)))
            i+=1
    except:
        pass
