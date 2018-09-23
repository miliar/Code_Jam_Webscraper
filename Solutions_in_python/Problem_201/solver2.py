import sys
import heapq
from math import log, ceil, floor

name = "C-small-2-attempt1"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    line = raw_input()
    line = line.split()
    n = int(line[0])
    k = int(line[1])

    level = int(ceil(log(k+1, 2)))

    # space = [n]
    # heapq._heapify_max(space)
    # i = 1
    # while(i<k):
    #     #room = space.pop(0)
    #     room = heapq.heappop(space)
    #     mid = (room + 1)/2
    #     if room % 2 == 0:
    #         if room - mid > 0:
    #             #space.(room - mid)
    #             heapq.heappush(space, room-mid)
    #         if mid - 1 > 0:
    #             #space.append(mid - 1)
    #             heapq.heappush(space, mid - 1)
    #         heapq._heapify_max(space)
    #     else:
    #         if mid - 1 > 0:
    #             #space.append(mid - 1)
    #             heapq.heappush(space, mid - 1)
    #         if room - mid > 0:
    #             #space.append(room - mid)
    #             heapq.heappush(space, room - mid)
    #         heapq._heapify_max(space)
    #     i += 1

    #room = heapq.heappop(space)
    left_room = n - (int(2**(level-1))-1)
    if k == 1:
        room = left_room
    else:
        last_level_nums = int(2**(level-1)- 2**(level-2))
        this_level_nums = int(2**(level)- 2**(level-1))
        if left_room <= this_level_nums:
            room = 1
        else:
            last_level_nums_total = 2**(level-1) -1
            this_level_nums_total = 2 ** (level) - 1
            if left_room % this_level_nums == 0:
                room = left_room / this_level_nums
            #elif k <= last_level_nums_total + (this_level_nums_total - last_level_nums_total)/2:
            elif k <= last_level_nums_total + (left_room % this_level_nums):
                room = int(ceil(float(left_room) / this_level_nums))
            else:
                room = int(floor(float(left_room) / this_level_nums))

    # elif left_room <=  2*(int(2**(level)) - int(2**(level-1))):
    #     room = 1
    # else:
    #     if left_room % (2*((int(2**(level-1)-1) - int(2**(level-2)-1)))):
    #         room = left_room / (2*((int(2**(level-1)-1) - int(2**(level-2)-1))))
    #     else:
    #         if k <= int(2**(level-1))-1 + (int(2**(level)) - int(2**(level-1)))/2:
    #             room = int(ceil(float(left_room) / (2 * ((int(2 ** (level - 1)-1) - int(2 ** (level - 2)-1))))))
    #         else:
    #             room = int(floor(float(left_room) / (2 * ((int(2 ** (level - 1)-1) - int(2 ** (level - 2)-1))))))

    #num_last_level = 2**(level-1) - 2**(level-2)
    #print "left is ", (n - (2**(level-1)-1))
    #room = (n - (2**(level-1)-1)) /  (num_last_level*2)
    #print "room is ", (n - (2 ** (level - 1) - 1))
    mid = (room+1)/2
    l = mid - 1
    r = room - mid
    print("Case #" + str(testCase) + ": " + str(max(l,r)) + " " + str(min(l,r)))