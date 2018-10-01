#
# Alec Grieser
# 13 April 2012
#
# For Google Code Jam qualifying round, "Dancing with Googlers" problem.
#

evals = None
data = open("B-small-attempt0.in", "r").read().split('\n')
fout = open("dancing.out", "w")

count = int(data[0])

def best_scores(to_go, position):
    global evals

    if to_go == 0:
        rtn = 0

        for x in range(position, len(evals)):
            rtn += evals[x][0]

        return rtn
    else:
        running = 0
        best = 0
        for x in range(position, len(evals) - to_go + 1):
            running += evals[x - 1][0] if x != position else 0

            if evals[x][1] != -1:
                best = max(best, running + best_scores(to_go - 1, x + 1)
                           + evals[x][1])

        return best          

for i in range(count):
    values = data[i + 1].split(' ')
    count = int(values[0])
    special = int(values[1])
    threshold = int(values[2])
    scores = [int(values[x + 3]) for x in range(count)]

    evals = []

    for j in range(len(scores)):
        if scores[j] % 3 == 0:
            if scores[j] == 0 or scores[j] == 30:
                evals.append((scores[j]//3 >= threshold, -1))
            else:
                evals.append((scores[j]//3 >= threshold,
                              scores[j]//3+1 >= threshold))
        elif scores[j] % 3 == 1:
            if scores[j] == 1:
                evals.append((scores[j]//3 + 1 >= threshold, -1))
            else:
                evals.append((scores[j]//3 + 1 >= threshold,
                              scores[j]//3+1 >= threshold))
        else:
            if scores[j] == 29:
                evals.append((scores[j]//3+1 >= threshold, -1))
            else:
                evals.append((scores[j]//3+1 >= threshold,
                              scores[j]//3+2 >= threshold))

    #print(evals)
    
    best = best_scores(special, 0)
    fout.write("Case #%d: %d\n" % (i + 1, best))
    print(best)
    
    
fout.close()


    
