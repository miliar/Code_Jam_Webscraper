#!/usr/bin/env python
import bisect
import sys

def main():
    fname, gname = sys.argv[1:3]
    with open(fname) as f, open(gname, 'w') as g:
        T = int(f.readline().strip())
        for case_num in range(1, T+1):
            N, X = map(int, f.readline().strip().split())
            sizes = map(int, f.readline().strip().split())
            result = get_result(sizes, X)

            g.write('Case #{}: {}\n'.format(case_num, result))
            
    return 0

# def get_result(sizes, capacity):
#     sizes = sorted(sizes)
#     used_indexes = set()
#     buckets = []
#     while sizes:
#         biggest = sizes.pop()
#         small_index = bisect.bisect(sizes, remaining_space, 0, i) - 1
#         curr_size = sizes[i]
#         curr_bucket = [curr_size]
#         used_indexes.add(i)
#         remaining_space = capacity - curr_size
#         while small_index >= 0 and small_index in used_indexes:
#             small_index -= 1
#         if small_index >= 0:
#             curr_bucket.append(small_index)
#             used_indexes.add(small_index)
#         buckets.append(curr_bucket)
#     assert len(used_indexes) == len(sizes)
#     return len(buckets)

def get_result(sizes, capacity):
    sizes = sorted(sizes)
    used_indexes = set()
    buckets = []
    for i in xrange(len(sizes)-1, -1, -1):
        if i in used_indexes:
            continue
        curr_size = sizes[i]
        curr_bucket = [curr_size]
        used_indexes.add(i)
        remaining_space = capacity - curr_size
        small_index = bisect.bisect(sizes, remaining_space, 0, i)-1
        while small_index >= 0 and small_index in used_indexes:
            small_index -= 1
        if small_index >= 0:
            curr_bucket.append(small_index)
            used_indexes.add(small_index)
        buckets.append(curr_bucket)
    assert len(used_indexes) == len(sizes)
    return len(buckets)

if __name__ == "__main__":
    status = main()
    sys.exit
