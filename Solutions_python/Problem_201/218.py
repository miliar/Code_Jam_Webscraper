def solve(n, k):
    cnt = {n: 1}
    before = k-1
    layer = 1
    while layer <= before:
        before -= layer
        next_cnt = {}
        for slot_size, slot_count in cnt.items():
            left = (slot_size) // 2
            right = (slot_size - 1) // 2
            next_cnt[left] = next_cnt.get(left, 0) + slot_count
            next_cnt[right] = next_cnt.get(right, 0) + slot_count
        cnt = next_cnt
        layer *= 2
    
    for slot_size in sorted(cnt.keys(), reverse=True):
        slot_count = cnt[slot_size]
        if slot_count <= before:
            before -= slot_count
        else:
            left = (slot_size) // 2
            right = (slot_size - 1) // 2
            return left, right


cases = int(input())
for c in range(cases):
    n, k = map(int, input().split())
    a, b = solve(n, k)
    print('Case #%d: %d %d' % (c+1, a, b))
