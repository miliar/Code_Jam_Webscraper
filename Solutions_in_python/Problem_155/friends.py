#!/usr/bin/python


def computeFriends(case):
    peopleUp = 0
    friends = 0
    print("===========")
    for index, shyNumber in enumerate(case):
        print("{} : {}".format(index, shyNumber))
        if index > peopleUp:
            friends += index - peopleUp
            peopleUp += index - peopleUp
        peopleUp += shyNumber

    print(friends)
    return friends


def compute(cases):
    friends = list()
    for case in cases:
        friends.append(computeFriends(case))

    return friends


if __name__ == "__main__":
    from parser import readfile, writeFile
    import sys
    friends = compute(readfile(sys.argv[1]))
    writeFile(friends, "output.txt")
