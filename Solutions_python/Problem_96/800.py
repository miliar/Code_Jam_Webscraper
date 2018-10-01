#!/usr/bin/env python
import sys

def get_possible_triplets(number, best_result_least):
    #all possible triplets for this number
    all = []
    for a in range(0, 11):
        for b in range(0, 11):
            for c in range(0, 11):
                if a+b+c == number:
                    #my new triplet
                    triplet = (a, b, c)

                    #build score-diff-list
                    triplet_set = list(set(list(triplet)))
                    score_diffs = []

                    if len(triplet_set) > 1:
                        score_diffs.append(abs(triplet_set[0] - triplet_set[1]))

                    if len(triplet_set) > 2:
                        score_diffs.append(abs(triplet_set[1] - triplet_set[2]))
                        score_diffs.append(abs(triplet_set[0] - triplet_set[2]))

                    #sort out impossible ones
                    #diff over 2 is always impossible
                    if len([x for x in score_diffs if x > 2]) > 0:
                        continue

                    #diff over 1 can exist only one time
                    if len([x for x in score_diffs if x > 1]) > 1:
                        continue

                    surprising = False

                    #2 only one time
                    if len([x for x in score_diffs if x == 2]) == 1 :
                        surprising = True

                    all.append(triplet + (surprising,))

    return all

def main():
    i = sys.stdin
    o = sys.stdout

    count = int(i.readline().strip())

    caseno = 1
    for line in i:
        if caseno > count:
            break

        ls = line.split()
        number_googlers = int(ls[0])
        number_surprising = int(ls[1])
        best_result_least = int(ls[2])

        googlers = [int(n) for n in ls[3:number_googlers + 3]]
        triplets = [get_possible_triplets(x, best_result_least) for x in googlers]
        max_result = 0

        #Walk through all possible series of triplets
        i = [0 for l in range(len(triplets))]
        while True:
            this_triplets = [triplets[g][x] for g,x in enumerate(i)]
            surprising_triplets = [x for x in this_triplets if x[3] == True]
            if len(surprising_triplets) == number_surprising:
                result_triplet = []
                for tr in this_triplets:
                    if len([x for x in tr if x >= best_result_least]) > 0:
                        result_triplet.append(tr)

                max_result = max(max_result, len(result_triplet))

            i[0] += 1
            exit = False
            for x in range(len(i)):
                if i[x] >= len(triplets[x]):
                    i[x] = 0
                    if x+1 < len(i):
                        i[x+1] += 1
                    else:
                        exit = True
            if exit:
                break


        o.write("Case #{0}: {1}\n".format(caseno, max_result))
        caseno = caseno + 1


if __name__ == '__main__':
    main()