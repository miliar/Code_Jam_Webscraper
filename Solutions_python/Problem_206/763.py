def solve(des, n, start, speed):
    if n == 1:
        res = des / ((des-start[0]) / speed[0])
        return res

    # else:
    #     if speed[0] >= speed[1] and start[0] >= start[1]:
    #         res = des / ((des-start[1]) / speed[1])
    #     if speed[0] < speed[1] and start[0] >= start[1]:
    #         a = (start[0]-start[1]) / (speed[1]-speed[0])
    #         b = (des-(start[0]+((start[0]-start[1])/(speed[1]-speed[0])*speed[0])))
    #         c = (des-(start[0]+((start[0]-start[1])/(speed[1]-speed[0])*speed[0]))) / speed[0]
    #         res = des / ((start[0]-start[1]) / (speed[1]-speed[0]) + (des-(start[0]+((start[0]-start[1])/(speed[1]-speed[0])*speed[0]))) / speed[0])
    #     if speed[0] >= speed[1] and start[0] < start[1]:
    #         res = des / ((des-start[1]) / speed[1])
    #     if speed[0] < speed[1] and start[0] < start[1]:
    #         res = des / ((des - start[0]) / speed[0])
    #     return res

    # minimum_speed = min(speed)
    # i = 0
    # minimum_start = float('inf')
    # while minimum_speed in speed:
    #     idx = speed.index(minimum_speed)
    #     corresponding_start = start[idx+i]
    #     if corresponding_start < minimum_start:
    #         minimum_start = corresponding_start
    #     speed.pop(idx)
    #     i += 1
    # res = des / ((des-minimum_start) / minimum_speed)
    # return res

    res = []
    for i in range(n):
        res.append((des-start[i]) / speed[i])
    result = des / max(res)
    return result


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        d, n = [int(s) for s in input().split(" ")]
        start = []
        speed = []
        for j in range(n):
            st, sp = [int(s) for s in input().split(" ")]
            start.append(st)
            speed.append(sp)
        result = solve(d, n, start, speed)
        print("Case #{}: {}".format(i, result))