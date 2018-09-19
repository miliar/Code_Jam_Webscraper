def comp1(a,b):
    if int(b)>int(a):
        return 1
    elif int(b)<int(a):
        return -1
    return 0

def comp2(a,b):
    if int(b)>int(a):
        return -1
    elif int(b)<int(a):
        return 1
    return 0

def main(f):
    cord = int(f.readline())

    a = f.readline().strip().split(' ')
    b = f.readline().strip().split(' ')

    a.sort(comp1)
    b.sort(comp2)

    sum = 0
    
    for x in zip(a,b):
        sum = sum + int(x[0])*int(x[1])

    return sum

f = open('A-large.in','r')
n = 1

for x in range(int(f.readline())):
    ans = main(f)
    print 'Case #'+str(n)+':',ans
    n = n + 1

