import sys

def solve_problem(mushrooms):
    eaten1 = 0
    eaten2 = 0
    previous_plate = None

    for plate in mushrooms:
        if previous_plate is None:
            previous_plate = plate
            continue
        if plate < previous_plate:
            eaten1 += previous_plate - plate
        previous_plate = plate

    rate = 0

    for i in xrange(len(mushrooms) - 1):
        rate = max(rate, mushrooms[i] - mushrooms[i+1])

    for i, plate in enumerate(mushrooms):
        if i == len(mushrooms) - 1:
            break
        eaten2 += min(rate, plate)

    return eaten1, eaten2

if __name__ == "__main__":
    num_of_cases = int(sys.stdin.readline().strip())

    for i in xrange(1, num_of_cases + 1):
        _ = sys.stdin.readline()
        mushrooms = map(int, sys.stdin.readline().split())
        eaten = solve_problem(mushrooms)
        print "Case #{0}: {1} {2}".format(i, *eaten)
