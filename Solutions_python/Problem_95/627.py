import sys
import string

if len(sys.argv) < 2:
    print "Usage: $(basename $0): input"
    exit()

translation_table = string.maketrans("ejpmyslckdxvnribtahwfougqz", "ourlangeismpbtdhwyxfckjvzq")

def translate(G):
    return G.translate(translation_table)

input = sys.argv[1]
f = open(input)
T = f.readline()
T = int(T)

for i in range(T):
    G = f.readline().strip("\n")
    S = translate(G)
    print "Case #%d: %s" % (i + 1, S)
