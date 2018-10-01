# python A.py < A-small-attempt0.in > A-small-attempt0.out
# 
# list(raw_input()) # List of chars
# [int(n) for n in raw_input().split()] # List of ints

if __name__ == "__main__":
    testcases = input()
    
    for case in xrange(1, testcases+1):
        
        counts = [int(n) for n in raw_input().split()[1]]
        extra_needed = 0
        total = 0
        for i in range(len(counts)):
            if total < i:
                extra_needed += i - total
                total = i
            total += counts[i]
        
        print("Case #%i: %s" % (case, str(extra_needed)))
