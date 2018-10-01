__author__ = 'wwang'
import heapq

def get_side_freespace(free_space):
    left_free_space = int(free_space/2)
    if free_space % 2 == 0:
        left_free_space -= 1
    return left_free_space, (free_space - left_free_space - 1)

def find_farest(N, K):
    if K == N:
        return "0 0"

    queue = []
    heapq.heappush(queue, -N)
    i = K
    left_free_space = 0
    right_free_space = 0
    while i > 0:
        free_space = -heapq.heappop(queue)
        left_free_space, right_free_space = get_side_freespace(free_space)
        # print(free_space, i, left_free_space, right_free_space)

        if left_free_space == 0 and right_free_space == 0:
            return "0 0"
        i -= 1
        heapq.heappush(queue, -left_free_space)
        heapq.heappush(queue, -right_free_space)


    return "%d %d" % (max(left_free_space, right_free_space), min(left_free_space, right_free_space))



t = int(input())  # read a line with a single integer
for ii in range(1, t + 1):
    input_array = input().split(' ')
    N = int(input_array[0])
    K = int(input_array[1])

    print("Case #%d: %s" % (ii, find_farest(N, K)))

# print(find_farest(500000, 240530))
# print(find_farest(500000, 127))
# print(find_farest(5, 2))