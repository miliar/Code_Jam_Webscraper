import sys
f = open(sys.argv[1])
n = int(f.readline())

for i in range(n):
    numbers = map(int, f.readline().strip().split())
    n_scores, surprising, target_score = numbers[:3]
    scores = numbers[3:]
    
    t = 0 #number with score >= p
    possible_surprises = 0
    for score in scores:
        max_nonsurprising = (score + 2) / 3
        max_surprising = -1
        if score >= 2 and score <= 28:
            max_surprising = (score + 4) / 3

        if max_nonsurprising >= target_score:
            t += 1
        elif max_nonsurprising < target_score and max_surprising >= target_score:
            possible_surprises += 1

    print "Case #%d: %d" % (i+1, t + min(possible_surprises, surprising))

    
