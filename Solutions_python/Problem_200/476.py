def N_to_digits(N):
    tmp = N
    result = []
    while tmp:
        result.append(tmp % 10)
        tmp /= 10
    result.reverse()
    return result

def digits_to_N(digits):
    result = 0
    for d in digits:
        result *= 10
        result += d
    return result

def tidyp(digits):
    return sorted(digits) == digits

def dec(digits, i):
    def rec(d, i):
        d[i] = 9
        if d[i-1] == 0:
            rec(d, i-1)
        else:
            d[i-1] -= 1
    d = digits[:]
    rec(d, i)
    while d[0]==0:
        d = d[1:]
    return d

def solve(N):
    cur = 0
    digits = N_to_digits(N)
    i = len(digits)-1
    while not tidyp(digits):
        digits = dec(digits, i)
        i -= 1

    return digits_to_N(digits)



def main():
    T = input()

    for i in range(T):
        N = input()
        print 'Case #{}:'.format(i+1), solve(N)

if __name__ == '__main__':
     main()
