T = 0
originalT = 0

def main():
    f = open('C-small-attempt0.in', 'r')
    o = open('output.out', 'w')
    T = int(f.readline())
    originalT = T
    for line in f:
        total = 0
        interval = line.split()
        lowerbound = int(interval[0])
        upperbound = int(interval[1])
        for num in xrange(lowerbound, upperbound + 1):
            total += FandSFinder(num, lowerbound, upperbound)
        o.write('Case #' + str(abs(T - originalT) + 1) + ': ' + str(total) + '\n')
        T -= 1
    f.close()
    o.close()

def FandSFinder(num, lowerbound, upperbound):
    total = 0
    string = str(num)
    sqstring = str(num**2)
    if string == string[::-1]:
        if num**2 <= upperbound and sqstring == sqstring[::-1]:
            total += 1
        candidateSqrt = int(num**0.5)
        if candidateSqrt < lowerbound and candidateSqrt**2 == num and str(candidateSqrt) == str(candidateSqrt)[::-1]:
            total += 1
        return total
    return 0

main()
