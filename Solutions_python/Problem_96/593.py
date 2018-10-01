import csv
import itertools

def jam(filename, mapper, num_args):
   " Generic helper to process Google Code Jam input file "
   with open(filename, 'rb') as f:
       reader = csv.reader(f)
       N = int(reader.next()[0])
       c = 0
       for arg0 in reader:
           c += 1
           args = arg0 + [reader.next() for _ in range(1, num_args)]
           yield mapper(*args)
       assert N == c, "Expected %s cases but found only %s" % (N, c)


# scores is a list of tuples from (0, 0, 0) to (10, 10, 10) 
scores = sorted(list(set(
    [tuple(sorted([a,b,c])) 
    for a in range(11) 
    for b in range(11) 
    for c in range(11)]
    )))

# split list of scores into list of not surprising and surprising
# results and discard what doesn't fit into either category

not_surprising = []
surprising = []

for s in scores:
    a,b,c = s
    ab = abs(a-b)
    ac = abs(a-c)
    bc = abs(b-c)
    if ab < 2 and ac < 2 and bc < 2:
        not_surprising.append(s)
    elif ab < 3 and ac < 3 and bc < 3:
        surprising.append(s)

# dictionaries mapping best score to list of total scores for
# surprise and non surprise scores

total_to_best = dict()
total_to_best_surprise = dict()

for s in not_surprising:
    total_to_best.setdefault(max(s), []).append(sum(s)) 

for s in surprising:
    total_to_best_surprise.setdefault(max(s), []).append(sum(s)) 

print total_to_best
print total_to_best_surprise

## that's all we need - let's process the input

def process(arg0):
    args = map(int, arg0.split())
    N, S, P = args[:3] 
    ts = args[3:]
    assert N == len(ts)

    not_surprising_totals = []
    surprising_totals = []

    for x in range(P, 11):
        not_surprising_totals += total_to_best.get(x, [])
        surprising_totals += total_to_best_surprise.get(x, [])

    count = 0
    for t in ts:
        if t in not_surprising_totals:
            count += 1
        elif t in surprising_totals and S > 0:
            count += 1
            S -= 1

    return count


with open('B.out', 'wb') as f:
    for i, r in enumerate(jam('B.in', process, 1)):
        response = "Case #%s: %s" % (i+1, r) 
        print response
        f.write(response)
        f.write('\n')
