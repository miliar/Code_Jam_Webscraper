import sys

g_to_s = { ' ':' ', 'y':'a', 'n':'b', 'f':'c', 'i':'d', 'c':'e', 'w':'f', 'l':'g', 'b':'h', 'k':'i', 'u':'j', 'o':'k', 'm':'l', 'x':'m', 's':'n', 'e':'o', 'v':'p', 'z':'q', 'p':'r', 'd':'s', 'r':'t', 'j':'u', 'g':'v', 't':'w', 'h':'x', 'a':'y', 'q':'z'}
t = int(sys.stdin.readline())

for i in range(1, t+1):
    g = sys.stdin.readline().strip()
#    g='ejp mysljylc kd kxveddknmc re jsicpdrysi'
    s=''
    for j in range(len(g)):
        s=s+g_to_s[g[j]]
    print 'Case #'+str(i)+': '+s
