import copy
import random

def solve_war(weights):
    counter = 0
    while len(weights[0]) != 0:
        naomi = weights[0].pop(0)
        for idx, w in enumerate(weights[1]):
            if w > naomi:
                weights[1].pop(idx)
                break
        if len(weights[0]) != len(weights[1]):
            counter += 1
            weights[1].pop(0)
    return counter

def solve_deceive(weights):
    counter = 0
    while len(weights[0]) != 0:
        naomi = weights[0].pop()
        ken = weights[1].pop()
        if ken > naomi:
            if len(weights[0]) != 0:
                weights[0].pop(0)
                weights[0].append(naomi)
        else:
            counter += 1
    return counter



input = open('input.txt', 'r')
output = open('output.txt', 'w')

num_of_test = int(input.readline().rstrip())
for i in range(1, num_of_test+1):
    num_weights = int(input.readline().rstrip())
    weights = []
    for k in range(0,2):
        instance = []
        line = input.readline().rstrip().split(' ')
        for j in range(0, num_weights):
            instance.append(float(line[j]))
        instance.sort()
        weights.append(instance)
    output.write('Case #%d: %d %d\n' %(i, solve_deceive(copy.deepcopy(weights)), solve_war(copy.deepcopy(weights))))


