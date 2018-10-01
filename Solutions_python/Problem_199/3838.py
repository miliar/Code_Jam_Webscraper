



def flip_k(pancakes, k, start):
    pancakes = list(pancakes)
    for i in range(start, k + start, 1):
        if pancakes[i] == '-':
            #print (pancakes)
            pancakes[i] = '+'
        else:
            pancakes[i] = '-'
    pancakes = "".join(pancakes)
    return pancakes


def flip(pancakes, k):
    queue = []
    done = []
    score = 0
    queue.append((pancakes, score))

    while len(queue) > 0:
        (pancakes, score) = queue.pop(0)
        if '-' not in pancakes:
            return score

        #if pancakes not in done:
            #done.append(pancakes)

            #enqueue next
        for i, item in enumerate(pancakes):
            if item == '-':
                for j in range(max(0, i - k + 1), min(i+1, len(pancakes) - k + 1), 1):
                    #print(pancakes, k, j)
                    flipped = flip_k(pancakes, k, j)
                    if flipped not in done:
                        done.append(flipped)
                        queue.append((flipped, score + 1))
                        #print (flipped)


    return -1

filename = 'in.txt'
f = open(filename, 'r')

lines = f.readlines()


cases = int(lines[0])

#print (lines)

for case in range(1, len(lines), 1):
    (pancakes, k) = lines[case].split()
    res = flip(pancakes, int(k))
    if res == -1:
        res = 'IMPOSSIBLE'
    print ('Case #' + str(case) + ":",  res)



