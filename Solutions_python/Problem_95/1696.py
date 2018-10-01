d = {'y':'a', 'n':'b', 'f':'c', 'i':'d', 'c':'e',
     'w':'f', 'l':'g', 'b':'h', 'k':'i', 'u':'j',
     'o':'k', 'm':'l', 'x':'m', 's':'n', 'e':'o',
     'v':'p', 'z':'q', 'p':'r', 'd':'s', 'r':'t',
     'j':'u', 'g':'v', 't':'w', 'h':'x', 'a':'y',
     'q':'z', ' ':' '}
T = int(input())
for i in range(1,T+1):
    result = [d[c] for c in input()]
    print("Case #"+str(i)+": "+(''.join(result)))
