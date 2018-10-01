def read_list_of(numtype):
    return map(numtype, raw_input().split())

def calculate(s):
    # s is 10001901
    stand = 0
    req = 0

    for shyness, n in enumerate(s):
        n = int(n)
        if n > 0 and shyness > stand:
            req += shyness - stand
            stand = shyness


        stand += n

    return req

def main():
    for case_number in xrange(int(raw_input())):
        s_big = raw_input()
        s = s_big.split()[1]

        result = calculate(s)

        print 'Case #%d: %s' % (case_number+1, result)

main()