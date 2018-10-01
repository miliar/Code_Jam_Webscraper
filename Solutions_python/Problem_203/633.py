  # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

import sys



f_dir = sys.argv[1]
fo_dir = sys.argv[2]

f = open(f_dir,'r')
fo = open(fo_dir,'w')

def greedy(xy,A,K):
    # to left:
    # print(xy,K)
    check = [xy]
    x = xy[0]
    y = xy[1]
    while y!=0:
        y-=1
        if A[x][y]=="?":
            A[x][y]=K
            check.append((x,y))
        else:
            break
    # to right:
    y = xy[1]
    while y!=len(A[x])-1:
        # print(x,y)
        y+=1
        if A[x][y]=="?":
            A[x][y]=K
            check.append((x,y))
        else:
            break
    # to up:
    x = xy[0]
    while x!=0:
        x-=1
        bol = True
        for xy in check:
            if A[x][xy[1]]!='?':
                bol = False
                break
        if not bol:
            break
        for xy in check:
            A[x][xy[1]]=K
    # to down:
    x = xy[0]
    while x!=len(A)-1:
        x+=1
        bol = True
        for xy in check:
            if A[x][xy[1]]!='?':
                bol = False
                break
        if not bol:
            break
        for xy in check:
            A[x][xy[1]]=K

t = int(f.readline())  # read a line with a single integer
test = []
count = 0
while count!=t:
  # n, m = [int(s) for s in f.readline().split(" ")]  # read a list of integers, 2 in this case
  # print("Case #{}: {} {}".format(i, n + m, n * m))
  # check out .format's specification for more formatting options
    # print(f.readline())
    s = f.readline().split()
    # print(s)
    l = int(s[0])
    A = []
    for i in range(l):
        A.append(list(f.readline()[:-1]))
    test.append(A)
    count+=1

f.close()

for A in test:
    # for row in A:
    #     print(row)
    parse=[]
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j]!='?' and A[i][j] not in parse:
                parse.append(A[i][j])
                greedy((i,j),A,A[i][j])


for i in range(1,len(test)+1):
    fo.write("Case #"+str(i)+':\n')
    for row in test[i-1]:
        fo.write(''.join(row)+'\n')

fo.close()