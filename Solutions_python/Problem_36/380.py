
import sys

#myfile = open('C-small-attempt0.in','r')
#myfile2 = open('C-small-attempt0.out','w')
myfile = open('C-large.in','r')
myfile2 = open('C-large.out','w')
sys.stdin = myfile
sys.stdout = myfile2

myword = 'welcome to code jam'
mydict = {}

def solve(word, word2):
    if len(word) < len(word2):
        return 0
    if len(word2) == 0:
        return 1
    if len(word) == 1:
        if len(word) == len(word2):
            if word == word2:
                return 1
            else:
                return 0
    if len(word2) == 1:
        if len(word) == len(word2):
            if word == word2:
                return 1
            else:
                return 0
        
    if mydict.has_key((word, word2)):
        return mydict[(word, word2)]
    
    if word[0] == word2[0]:
        mydict[(word, word2)] = (solve(word[1:],word2[1:]) + solve(word[1:],word2)) % 10000
    else:
        mydict[(word, word2)] = solve(word[1:],word2) % 10000
    
    return mydict[(word, word2)]


num = int(sys.stdin.readline())

for case in xrange(num):
    line = sys.stdin.readline().strip()
    mydict = {}
    res = solve(line,myword)
    print "Case #%d: %04d" % (case+1,res)

myfile.close()
myfile2.close()