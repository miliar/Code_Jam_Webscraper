import sys

for c in xrange(int(sys.stdin.readline())):
    result = "X"

    choice1 = int(sys.stdin.readline())
    arr1 = []
    for i in range(4):
        arr1 += [sys.stdin.readline().strip().split()]

    choice2 = int(sys.stdin.readline())
    arr2 = []
    for i in range(4):
        arr2 += [sys.stdin.readline().strip().split()]

    res = set(arr1[choice1-1]).intersection( set(arr2[choice2-1]))


    if res == set([]):
        result = "Volunteer cheated!"
    elif len(res) > 1:
        result = "Bad magician!"
    else:
        result = str(res.pop())

    print "Case #"+str(c+1)+": "+result   
