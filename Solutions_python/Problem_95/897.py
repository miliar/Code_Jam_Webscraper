trans = {'\n':'\n',' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o',
         'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x',
         'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k',
         'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't',
         'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
def run():
    f=open("input.in")
    g=open("out.txt",'w')
    num = int(f.readline())
    for i in range(num):
        g.write("Case #%d: " % (i+1))
        g.write(cip(f.readline()))
        continue
    f.close()
    g.close()


alpha = " abcdefghijklmnopqrstuvwxyz"
def helper():
    for x in alpha:
        print "'"+x+"':'"+x+"', ",

def cip(text):
    return "".join([trans[x] for x in text])

def modify(clear,code):
    for i in range(len(clear)):
        trans[code[i]]=clear[i]

        
