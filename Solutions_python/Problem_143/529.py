import fileinput
from collections import deque

def naive_answer(A, B, K):
    num = 0
    for i in range(A):
        for j in range(B):
            if ((i & j) < K):
                num += 1

    return num

num_inputs = 0
lines = deque()

for line in fileinput.input():
    lines.append(line)

num_inputs = int(lines.popleft())

# Get inputs
for i in range(num_inputs):
    line = lines.popleft().strip()
    nums = line.split(' ')
    A = int(nums[0])
    B = int(nums[1])
    K = int(nums[2])

    answer = naive_answer(A, B, K)
    print('Case #'+str(i+1)+': ' + str(answer))