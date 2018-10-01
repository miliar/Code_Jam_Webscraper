import fileinput
import sys
sys.setrecursionlimit(10000)
pancake_flip_map = {'+': '-', '-': '+'}
def flip(pancakes, k, index):
    pancakes = pancakes[0:index], pancakes[index:index+k],\
               pancakes[index+k:]
    pancakes = \
        pancakes[0] + \
        ''.join([pancake_flip_map[i] for i in pancakes[1]]) + \
        pancakes[2]
    return pancakes

assert flip('---', 3, 0) == '+++'
assert flip('+---', 3, 1) == '++++'
assert flip('+---+',3,1) == '+++++'
assert flip('+-----+',3,2)== '+-+++-+'


IMPOSSIBLE = 'IMPOSSIBLE'
def f(pancakes, k):
    if pancakes.count('+') == len(pancakes):
        return 0#0 flips
    elif len(pancakes) < k and '-' in pancakes:
        return IMPOSSIBLE

    if pancakes[0] == '-':
        out = f(flip(pancakes[:k], k, 0) + pancakes[k:], k)
        if out == IMPOSSIBLE:
            return out
        else:
            return 1 + out
    else:
        return f(pancakes[1:], k)
    

#cases = [('---+-++-', 3), ('+++++', 4), ('-+-+-', 4)]
#answers = [3, 0, IMPOSSIBLE]
#for index, cases in enumerate(cases):
#    pancakes, k = cases
#    answer = answers[index]
#    assert f(pancakes, k) == answer

'''
file = open('/Users/michael/Downloads/A-small-attempt0.in').readlines()
file = file[1:]
for index, line in enumerate(file):
    line = line.strip()
    pancakes, k = line.split()
    k = int(k)
    print("Case #{}: ".format(1+index) + str(f(pancakes, k)))
'''
i = 0
for line in fileinput.input():
    if i == 0:
        i += 1
        continue
    line = line.strip()
    pancakes, k = line.split()
    k = int(k)
    index = i
    print("Case #{}: ".format(index) + str(f(pancakes, k)))
    i += 1
