import fileinput

from collections import deque

def read_input():
    total = 0
    in_file = fileinput.input()
    tc_count = int(in_file.readline())
    for i in range(tc_count):
        rounds_count, seats_count, groups_count = (int(x) for x in in_file.readline().split())
        groups = deque([int(x) for x in in_file.readline().split()])
        assert groups_count == len(groups)
        print "Case #" + str(i+1) + ": " + str(solve(rounds_count, seats_count, groups))

def solve(rounds, seats, groups):
    if sum(groups) <= seats:
        return sum(groups) * rounds
    euros = 0
    for r in range(rounds):
        people = 0
        while people + groups[0] <= seats:
            people += groups[0]
            groups.rotate(-1)
        euros += people    
    return euros;

def main():
    read_input()


if __name__ == '__main__':
    main()

