def lastTidyNumber(N):
    if isTidy(N):
        return N

    digits = [int(i) for i in list(str(N))] # N = 321, digits = [1, 2, 3]
    size = len(digits)
    ret = [0 for i in xrange(size)]
    for i in xrange(size-1, 0, -1): #reversed indices
        if digits[i-1] > digits[i]:
            digits[i-1] -= 1
            ret[i-1] = digits[i-1]
            ret[i] = 9
        else:
            ret[i-1] = digits[i-1]

    for i in xrange(size-1):
        if ret[i] > ret[i+1]:
            ret[i+1] = 9

    return int("".join([str(i) for i in ret]))

def isTidy(N):
    digits = [int(i) for i in list(str(N))]
    for i in range(len(digits)-1):
        if digits[i] > digits[i+1]:
            return False
    return True

# def tests():
#     print(lastTidyNumber(132) == 129)
#     print(lastTidyNumber(1000) == 999)
#     print(lastTidyNumber(7) == 7)
#     print(lastTidyNumber(111111111111111110) == 99999999999999999)

# tests()

def main():
    num_problems = int(raw_input())
    for i in xrange(1, num_problems+1):
        N = raw_input()
        print "Case #{}: {}".format(i, lastTidyNumber(N))

if __name__ == "__main__":
    main()