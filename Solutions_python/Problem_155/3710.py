import os

# Determine the number of test cases
with open(os.path.expanduser('~/Downloads/A-small-attempt1.in'), 'r') as f:
    n_cases = int(f.readline())

def test_ovation(d, shyness, t):
    needed = [0]
    for k in range(0, len(shyness)):
        if d[k] < k+1:
            needed.append(k+1 - d[k])
    with open('output.txt', 'a') as f:
        f.write("Case #%s: %s" % (t, max(needed)))

for t in xrange(1, (n_cases + 1)):
    f = open(os.path.expanduser('~/Downloads/A-small-attempt1.in'))
    for i, l in enumerate(f):
        if i == t:
            shyness = list(l[2:-1])
            d = {k: 0 for k in range(0, len(shyness))}
            for k in range(0, len(shyness)):
            # Initialize a dictionary with the number of people that would be standing
            # if everyone at each level stood up.
                if k == 0:
                    d[k] += int(shyness[k])
                else:
                    d[k] += (d[k-1] + int(shyness[k]))
            test_ovation(d, shyness, t)
            if t < n_cases + 1:
                with open('output.txt', 'a') as f:
                    f.write('\n')
