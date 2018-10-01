import string

fname = 'A-small-attempt0'
f = open('/Users/evolz/codejam/%s.in' % fname, 'r')
lines = []
noc = 0 # no of cases
mapping = {'a':'y',
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
           '\n':''
           }
for line in f.readlines():
    lines.append(line)
noc = int(lines[0])
result = []
i = 1
for line in lines[1:]:
    text = ''
    for c in line:
        text += mapping[c]
    result.append('Case #%s: %s' % (i, text))
    i += 1
f.close()
#print string.join(result, '\n')

f = open('/Users/evolz/codejam/%s.out' % fname, 'w')
f.write(string.join(result, '\n'))
f.close()
print string.join(result, '\n')
