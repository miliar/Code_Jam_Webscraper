# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer

def tidynumber(n):
    number = str(n)
    if len(number) == 1:
        return True
    first = int(number[0])
    second = int(number[1])
    if first > second:
        return False
    else:
        recurse = int(number[1:])
        return tidynumber(recurse)

def tidyloop(n):
    array=[]
    for i in range(0,n+1):
        if tidynumber(i):
            array.append(i)
    return array[-1]

for i in xrange(1, t + 1):
    n = int(raw_input())
    m = tidyloop(n)
    print "Case #{}: {}".format(i, m)
  # check out .format's specification for more formatting options
