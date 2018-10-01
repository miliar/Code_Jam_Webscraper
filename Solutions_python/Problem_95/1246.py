dict = {
 'a':'y',
 'b':'h',
 'c':'e',
 'd':'s',
 'e':'o',
 'f':'c',
 'g':'v',
 'h':'x',
 'i':'d',
 'j':'u',
 'k':'i',
 'l':'g',
 'm':'l',
 'n':'b',
 'o':'k',
 'p':'r',
 'q':'z',
 'r':'t',
 's':'n',
 't':'w',
 'u':'j',
 'v':'p',
 'w':'f',
 'x':'m',
 'y':'a',
 'z':'q',
 ' ':' ',
}

f = open('a.in','r')
cases = int(f.readline())
for j in range(cases):
    out = ""
    line = f.readline().rstrip()
    for i in range(len(line)):
        out += dict[line[i]]
    print("Case #" + str(j+1) + ": " + out)