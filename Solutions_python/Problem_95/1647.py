m = { 'a':'y',
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
  'z':'q'}
t = int(raw_input())
for c in xrange(t):
    s = raw_input()
    r = ''
    for i in s:
        if i == ' ':
            r += i
        else:
            r += m[i]
    print 'Case #' + str(c+1) +': ' + r

    
