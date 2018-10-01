
dict = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm','q':'z', 'z':'q'}

def solve():
    msg = raw_input() 
    plain = ''
    for c in msg:
        if c in dict:
           plain += dict[c]
        else:
           plain += ' '
    return plain
if __name__ == '__main__':
    t = int(raw_input())
    for case in range(1, t+1):
        print("Case #{0}: {1}".format(case, solve()))


