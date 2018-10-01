tc_num = int(input())

def flip_pancake(pancake, p_pos, p_len):
    s = p_pos - p_len + 1
    e = p_pos + 1
    flipped = ['+' if p == '-' else '-' for p in pancake[s:e]]
    head = pancake[:s]
    mid = ''.join(flipped)
    tail = pancake[e:]
    return head + mid + tail

for i in range(0, tc_num):
    pancake, flip_size = input().split(' ')
    flip_size = int(flip_size)
    flip_count = 0

    rpos = pancake.rfind('-', 0, len(pancake))
    while rpos >= flip_size - 1:
        pancake = flip_pancake(pancake, rpos, flip_size)
        flip_count += 1
        rpos = pancake.rfind('-', 0, len(pancake))

    if rpos != -1:
        print("Case #{}: IMPOSSIBLE".format(i + 1))
    else:
        print("Case #{}: {}".format(i + 1, flip_count))

