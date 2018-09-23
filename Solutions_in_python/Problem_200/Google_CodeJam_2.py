def ordertest(A):
    for i in xrange(len(A) - 1):
        if A[i] > A[i+1]:
            return False

    return True

def concat(numList):
    s = ''.join(map(str, numList))
    return int(s)

def HappyNumber(N, case_number):
    for i in xrange (N,0, -1):
        arr = [int(d) for d in str(i)]
        
        if (ordertest(arr) == True):
            f = open('output.txt', 'w')
            print "Case #" + str(case_number) + ": " + str(concat(arr)) + "\n"
            break

with open('B-small-attempt1.in', 'r') as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

T = content[0]

for i in xrange(1, T+1):
    HappyNumber(content[i], i)

