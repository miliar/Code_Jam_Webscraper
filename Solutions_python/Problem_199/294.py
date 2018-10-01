import time

"""It suffices to use the naive greedy algorithm.
But we can also do it using this O(n log(n)) algorithm:

Segment tree algorithm: rewrite the problem as :) are even numbers, :( are odd numbers.
The target is to get everything to even numbers.
Denote the original array as O, denote the auxilliary as A.
Let O be the prefix sum of A, i.e. O[i] = A[0] + ... + A[i], or A[i] = O[i] - O[i - 1].
Insert A into a binary indexed tree.
We can increment an element in A in O(log(n)) time, we can get the i-th prefix sum of A in O(log(n)) time.
We don't explicitly maintain O, but rather use A to represent O.
From left to right, we only flip pancake if prefix_sum(A, i) is odd, in which case, we want to increment O[i..<i+k] by 1 <=> increment A[i] and A[i + k].

Much more sophisticated, and not trivial to implement.
"""

def MinimumNumberOfFlips(nums, k):
  """Returns the minimum number of flips needed to flip S to all +.
  The algorithm is to greedily flip the pancakes from left to right.

  Args:
    nums: An array representing the pancakes
    k: The size of the flipper

  Returns:
    min_num: The minimum number of flips required, 'impossible' if not possible
  """
  min_num = 0 # return value
  N = len(nums)
  for idx in range(N - k + 1):
    if nums[idx]:
      min_num += 1
      for j in range(idx, idx + k):
        nums[j] = 1 - nums[j]
  for idx in range(N - k + 1, N):
    if nums[idx]: return 'IMPOSSIBLE'
  return min_num

start_time = time.time()
n_test_case = int(input())
for i in range(1, n_test_case + 1):
  S, k = input().split(' ')
  k = int(k)
  nums = [0 if x == '+' else 1 for x in S]
  min_num = MinimumNumberOfFlips(nums, k)
  print('Case #{}: {}'.format(i, min_num))
with open('time.log', 'w') as f:
  f.write('--- %s seconds ---' % (time.time() - start_time))
  f.close()
