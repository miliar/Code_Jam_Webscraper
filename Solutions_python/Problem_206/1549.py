import sys

sys.setrecursionlimit(1000000)


def solveList(problem, d):

    if len(problem) == 0:
        return 0

    myMinTime = (d - problem[0]['pos']) / float(problem[0]['speed'])
    hisMinTime = solveList(problem[1:], d)

    return max(myMinTime, hisMinTime)

def main():

    numToCheck = []

    for i in range(int(raw_input())):

        newList = []

        d, length = raw_input().split(' ')

        for i2 in range(int(length)):
            pos, speed = raw_input().split(' ')

            newList.append({"pos": int(pos), "speed": int(speed)})

        numToCheck.append({"d": int(d), "length": int(length), "list": newList})

    count = 0
    for problem in numToCheck:
        count += 1
        ret = problem['d'] / solveList(problem['list'], problem['d'])

        print("Case #{}: {:.6f}".format(count, ret))


if __name__ == "__main__":
    main()