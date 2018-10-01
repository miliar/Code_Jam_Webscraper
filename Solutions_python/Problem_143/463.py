# Google Code Jam 2014 Round 1B
# Problem B
# Shaotong Wang

fin = open('B.in', 'r')
fout = open('B.out', 'w')

num_cases = int(fin.readline())

for case in range(1,num_cases+1):
    a, b, k = map(int, fin.readline().split())
    res = 0
    for i in xrange(a):
        for j in xrange(b):
            if i&j < k:
                res = res + 1
    fout.write("Case #" + str(case) + ": " + str(res) + "\n")


fin.close()
fout.close()

