#http://stackoverflow.com/questions/9453820/alternative-to-python-string-item-assignment
class Charray(list):

    def __init__(self, mapping=[]):
        "A character array."
        if type(mapping) in [int, float, long]:
            mapping = str(mapping)
        list.__init__(self, mapping)

    def __getslice__(self,i,j):
        return Charray(list.__getslice__(self,i,j))

    def __setitem__(self,i,x):
        if type(x) <> str or len(x) > 1:
            raise TypeError
        else:
            list.__setitem__(self,i,x)

    def __repr__(self):
        return "charray['%s']" % self

    def __str__(self):
        return "".join(self)

def DebugPrint(s, x):
    print "DEBUG(" + s + ") " + str(x)

def IsTidy(n):
    s = str(n)
    last = 0
    for c in s:
        if int(c) < last:
            return False
        last = int(c)
    return True

def LastTidy(n):
    tmp = n
    while True:
        if IsTidy(tmp):
            DebugPrint("SUCCESS", tmp)
            return int(tmp);
        tmp = tmp - 1
        
LastTidy(132)
LastTidy(1000)
LastTidy(7)

def TidyToIdx(n):
    s = str(n)
    for i in range(1, len(s) + 1):
        #DebugPrint("s", s[:i])
        if not IsTidy(s[:i]):
            return i - 1
    return None;

def LastTidy2(n):
    while True:
        DebugPrint("n", n)
        if IsTidy(n):
            DebugPrint("Success2", n)
            return n
        
        s = str(n)
        i = TidyToIdx(n)
        DebugPrint("i", i)
        pos = len(s) - i
        DebugPrint("pos", pos)
        x = pow(10, pos)
        #oldval = str(int(s[i-1]) - 1)
        #DebugPrint("oldval", oldval)
        DebugPrint("x ", x)
        n -= x
        s2 = str(n)
        while len(s2) < len(s):
            s2 = '0' + s2
        c = Charray(s2)
        DebugPrint("cb", c) 
        for j in range(i, len(c)):
            c[j] = '9'
        DebugPrint("ca", c) 
        n = int(str(c))
        
LastTidy2(111111111111111110)
LastTidy2(230946702394767474)
LastTidy2(102123895219028353)
LastTidy2(992347681293768533)
LastTidy2(1000)

import sys
import math
import string

def solve(S):
    return LastTidy2(int(S))
    
def main():
    if (not len(sys.argv) == 3):
        print("Need exactly twos args: input filename and output filename")
        return
    input_data = open(sys.argv[1], 'r').read()
    output_file = open(sys.argv[2], 'w')
    split_input = input_data.split("\n")
    case_count = int(split_input[0])
    for i in range(0,case_count):
        res = solve(split_input[i+1])
        DebugPrint("Case #", i+1)
        output_file.write("Case #" + str(i+1) + ": " + str(res) + "\n")
    
if __name__ == "__main__":
    main()
