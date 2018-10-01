import heapq

import datetime


def interval_len(interval):
    return interval[1] - interval[0]


def add_interval(start, end):
    if end < start:
        return (end, end)
    else:
        return (start, end)


def solve():
    mul_factor = 1e7
    t = int(raw_input())
    for i in range(t):
        n, k = map(int, raw_input().split(' '))
        if n == k:
            print 'Case #{}: {} {}'.format(i + 1, 0, 0)
            continue
        if k == 1:
            print 'Case #{}: {} {}'.format(i + 1, n / 2, (n - 1) / 2)
            continue
        intervals = [(0, n)]
        interval_heap = []
        heapq.heappush(interval_heap, (-mul_factor * n, 0))
        interval_idx = 0
        for j in range(k):
            _, largest_interval_idx = heapq.heappop(interval_heap)
            largest_interval = intervals[largest_interval_idx]
            interval_length = interval_len(largest_interval)
            if interval_length % 2 == 0:
                partition_idx = (interval_length - 1) / 2
            else:
                partition_idx = interval_length / 2
            left_interval = add_interval(largest_interval[0], largest_interval[0] + partition_idx)  # [:partition_idx]
            right_interval = add_interval(largest_interval[0] + partition_idx + 1,
                                          largest_interval[1])  # largest_interval[partition_idx + 1:]
            left_offset = left_interval[0] if len(left_interval) > 0 else 0
            right_offset = right_interval[0] if len(right_interval) > 0 else 0
            heapq.heappush(interval_heap,
                           (mul_factor * -interval_len(left_interval) + left_offset, interval_idx + 1))
            heapq.heappush(interval_heap,
                           (mul_factor * -interval_len(right_interval) + right_offset, interval_idx + 2))
            interval_idx += 2
            intervals.append(left_interval)
            intervals.append(right_interval)

        print 'Case #{}: {} {}'.format(i + 1, max(interval_len(left_interval), interval_len(right_interval)),
                                       min(interval_len(left_interval), interval_len(right_interval)))


solve()
