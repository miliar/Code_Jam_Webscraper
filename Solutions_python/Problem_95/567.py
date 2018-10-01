import string, sys

s_chr = 'abcdefghijklmnopqrstuvwxyz'
ggl_chr = 'yhesocvxduiglbkrztnwjpfmaq'
trans = string.maketrans(s_chr, ggl_chr)
f = sys.stdin
T = int(f.readline())

for i in range(T):
    g = f.readline().strip()
    
    print 'Case #{}:'.format(i+1),g.translate(trans)
