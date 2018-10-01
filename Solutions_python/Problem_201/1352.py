"""
import math

T = int(raw_input().strip())
for t in range(T):
    N, K = [int(item) for item in raw_input().strip().split()]

    slots = list()
    if N > 1:
        slots.append(N)

    answer = (0, 0,)

    i = 1
    while i <= K and len(slots) > 0:
        biggest_slot = max(slots)
        slots.remove(biggest_slot)
        biggest_slot -= 1
        answer = (int(math.ceil(biggest_slot / 2.0)), int(math.floor(biggest_slot / 2.0)),)
        for num in answer:
            if num > 1:
                slots.append(num)
        print(i, biggest_slot, answer)
        i += 1

    if i == K + 1:
        print('Case #{:d}: {:d} {:d}'.format(t + 1, answer[0], answer[1]))
    else:
        print('Case #{:d}: 0 0'.format(t + 1))

"""


import math

T = int(raw_input().strip())
for t in range(T):
    N, K = [int(item) for item in raw_input().strip().split()]

    slots = dict()
    if N > 1:
        slots[N] = 1

    answer = (0, 0,)

    i = 1
    while i <= K and len(slots) > 0:
        biggest_slot = max(slots)
        num_biggest_slot = slots[biggest_slot]
        del slots[biggest_slot]
        biggest_slot -= 1
        answer = (int(math.ceil(biggest_slot / 2.0)), int(math.floor(biggest_slot / 2.0)),)
        for num in answer:
            if num > 1:
                if num not in slots:
                    slots[num] = num_biggest_slot
                else:
                    slots[num] += num_biggest_slot
        i += num_biggest_slot

    if i > K:
        print('Case #{:d}: {:d} {:d}'.format(t + 1, answer[0], answer[1]))
    else:
        print('Case #{:d}: 0 0'.format(t + 1))
