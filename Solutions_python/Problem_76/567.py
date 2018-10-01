filename = 'small'

sum_p = lambda c: reduce(lambda x, y: x ^ y, c)
sum_s = lambda c: sum(c)

def solve(candies):
    if sum_p(candies) != 0:
        return 'NO'
    candies.sort()
    major = None
    for end_s in xrange(len(candies), 0, -1):
        for start_s in xrange(end_s - 1, -1, -1):
            candies_s = candies[start_s:end_s]
            candies_p = candies[:start_s] + candies[end_s:]
            if candies_p == []:
                continue
            if sum_p(candies_s) == sum_p(candies_p) and (major == None or sum_s(candies_s) > major):
                major = sum_s(candies_s)
    
    return str(major) if major != None else 'ERROR'

def main():
    file_in = open('C-%s.in' % filename)
    file_out = open('C-%s.out' % filename, 'w')
    cases = int(file_in.readline().strip())
    for case in xrange(1, cases + 1):
        qtd_candies = int(file_in.readline().strip())
        result = solve(map(int, file_in.readline().strip().split(' ')))
        file_out.write('Case #%d: %s\n' % (case, result))
    file_out.close()
    file_in.close()
    return

if __name__ == '__main__':
    main()
    import sys
    sys.exit(0)
