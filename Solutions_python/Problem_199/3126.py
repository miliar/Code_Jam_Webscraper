import pdb

input_file = 'A-large.in'
input = open(input_file)
lines = input.readlines()
input.close()

N = int(lines[0][:-1])


def flip(pancake):
    return {'+': '-',
            '-': '+'}[pancake]


def solve(pancakes, k):
    pancakes = list(pancakes)
    n = len(pancakes)
    count = 0
    for i in xrange(n - k):
        if pancakes[i] == '-':
            pancakes[i: i + k] = map(flip, pancakes[i: i + k])
            count += 1
    final_set = pancakes[n - k:]
    if final_set == ['+'] * k:
        return count
    elif final_set == ['-'] * k:
        return count + 1
    else:
        return 'IMPOSSIBLE'
        

output_file = 'A-large.out'
output = open(output_file, 'wb')
for i, line in enumerate(lines[1:]):
    pancakes, k = line.strip().split(' ')
    ans = solve(pancakes, int(k))
    output.write('Case #{i}: {ans}\n'.format(i=i+1, ans=ans))
output.close()
