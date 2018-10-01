from sys import stdin, stdout

def solve(cost, fps, goal):
    # print("Cost: {}".format(cost))
    # print("Fps: {}".format(fps))
    # print("goal: {}".format(goal))

    farms = 0
    cps = 2.0
    time = 0.0

    cur = goal / cps

    while True: # TODO some bound on farms
        next = time + goal / cps
        if next > cur:
            return cur
        else:
            cur = next
        time += cost / cps
        cps += fps
        farms += 1


def main():
    lines = stdin.readlines()

    t = int(lines[0])
    lines = lines[1:]

    for test in range(t):
        [C, F, X] = [float(s) for s in lines[0].split()]
        lines = lines[1:]
        print("Case #{}: {}".format(test + 1, solve(C, F, X)))

main()
