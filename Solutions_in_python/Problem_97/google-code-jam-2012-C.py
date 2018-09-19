import sys
import string

if len(sys.argv) < 2:
    print "Usage: $(basename $0): input"
    exit()

input = sys.argv[1]
f = open(input)
T = f.readline()
T = int(T)

if T < 1 or T > 50:
    print "T is out of range"
    exit()

N_max = 2000000

def n_digits(n):
    if n == 0:
        return 1
    digits = 0
    while n > 0:
        digits += 1
        n = n / 10
    return digits

# maximum n of 6!
def exp_10(n):
    if n == 6:
        return 1000000
    elif n == 5:
        return 100000
    elif n == 4:
        return 10000
    elif n == 3:
        return 1000
    elif n == 2:
        return 100
    elif n == 1:
        return 10
    else:
        return 1

def cycle(n, digits_in_n):
    return n / 10 + n % 10 * 10**(digits_in_n-1)

def recycled_pairs_in_range(A, B):
    pairs = 0

    for n in range(A, B + 1):
        c = n  # pair candidate
        digits = n_digits(n)
        pairs_of_n = {}
        for i in range(digits - 1):
            c = cycle(c, digits)
            if c >= A and c <= B and c > n:
                pairs_of_n[c] = 1
        pairs += len(pairs_of_n)
    return pairs

for i in range(T):
    s = f.readline().strip("\n").split(" ")
    A = int(s[0])
    B = int(s[1])

    if A < 1 or B < 1 or A > N_max or B > N_max:
        print "A or B is out of range"
        exit()
    
    pairs = recycled_pairs_in_range(A, B)
    print "Case #%d: %d" % (i + 1, pairs)
