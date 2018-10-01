from itertools import combinations

def run(values):
    n = len(values)
    seans_worth = []
    most_sean_value = 0
    for i in range(n - 1):
        combs = combinations(values, i + 1)
        for comb in combs:
            sean = comb
            patrick = list(values)
            for i in sean:
                patrick.remove(i)
            sean_val = sum(sean)
            if sean_val >= sum(patrick):
                seans_worth.append((sean, patrick))
            most_sean_value = max(most_sean_value, sean_val)
    patricks_worth = []
    patricks_sum = lambda x, y: x ^ y
    for sean, patrick in seans_worth:
        sean_val = reduce(patricks_sum, sean)
        patrick_val = reduce(patricks_sum, patrick)
        if patrick_val == sean_val:
            patricks_worth.append((sean, patrick))
            break
    if not patricks_worth:
        return "NO"
    return most_sean_value
            
if __name__ == "__main__":
    n = int(raw_input())
    for i in range(n):
        n_candies = raw_input()
        candies = raw_input().split()
        candies = [int(c) for c in candies]
        print "Case #%d: %s" % (i + 1, run(candies))
