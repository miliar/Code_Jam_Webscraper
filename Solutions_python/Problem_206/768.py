f = open("cruise_control.txt")

def input2():
       res = f.readline()
       return res


def get_max_speed():
    # loop from the end though horses
        # find the time Ti it needs to reach destination
        # if Ti < Ti-1
        #   find the time-place M where Hi catches up with Hi-1, rest of the way Vi = Vi-1, update Ti

    # velocity, start point
    MAX_INT = 10 ** 10
    prev_t = 0
    prev_s = D
    prev_v = MAX_INT
    for s, v in horses:
        t = (D - s) / v
        if t < prev_t:
            delta_t = (prev_s - s) / (v - prev_v)
            delta_s = D - (prev_s + prev_v * delta_t) # the rest of the way
            t = delta_t + delta_s / prev_v

        prev_t = t
        prev_v = v
        prev_s = s


    return D / prev_t

T = int(input().strip())

for t in range(T):
    D, H = [int(x) for x in input().strip().split(' ')]

    horses = [None] * H # array of pairs (start pos, velocity)
    for h in range(H):
        horses[h] = [int(x) for x in input().strip().split(' ')]
    horses.sort(key = lambda x: x[0], reverse = True)

    res = 0
    res = get_max_speed()

    print("Case #{}: {}".format(t + 1, res))