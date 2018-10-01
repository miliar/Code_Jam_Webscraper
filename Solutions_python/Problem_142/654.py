import sys
sys.stdin = open('in')
sys.stdout = open('out', 'w')


def strip_dupes(string):
    result = string[0]
    last_letter = result
    for letter in string:
        if letter != last_letter:
            result += letter
            last_letter = letter
    return result

def min_cost(strings):
    canonical = strip_dupes(strings[0])
    counters = [[] for s in strings]
    for i, s in enumerate(strings):
        counter = counters[i]
        ci = 0
        count = 0
        for letter in s:
            if canonical[ci] != letter:
                ci += 1
                # print count, letter
                counter.append(count)
                count = 0
            count += 1
        counter.append(count)
    # print counters
    total_cost = 0
    for i, letter in enumerate(canonical):
        cost = 0
        for counter in counters:
            cost += counter[i]
        avg = int(round(cost / float(len(strings))))
        cost = 0
        for counter in counters:
            cost += abs(counter[i] - avg)
        total_cost += cost
    return total_cost

for case in xrange(int(raw_input())):
    num_strings = int(raw_input())
    strings = []
    for i in xrange(num_strings):
        strings.append(raw_input())

    dupeless = map(strip_dupes, strings)
    if all(x == dupeless[0] for x in dupeless):
        # compute dist as lowest cost for each letter
        cost = min_cost(strings)
        print("Case #{}: {}".format(case + 1, cost))
    else:
        print("Case #{}: Fegla Won".format(case + 1))

# main()
