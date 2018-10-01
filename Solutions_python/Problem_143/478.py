import sys

# Set up the input and output files
f = sys.argv[1]
sys.stdin = open(f, 'r')
sys.stdout = open(f[:-2] + "out", 'w')

# Read in T
total_cases = int(input())
for case_number in range(1, total_cases + 1):
    # Read in C and W
    a, b, k = [int(n) for n in input().strip().split()]
    pairs = 0
    for i in range(a):
        for j in range(b):
            if i & j < k:
                pairs += 1


    print('Case #{0}: {1}'.format(case_number, pairs))


