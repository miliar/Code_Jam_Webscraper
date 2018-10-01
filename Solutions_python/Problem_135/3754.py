def solution(possible_numbers):
    if len(possible_numbers) == 0:
        return "Volunteer cheated!"
    elif len(possible_numbers) == 1:
        return list(possible_numbers)[0]
    else:
        return "Bad magician!"

def main():
    t = int(raw_input())

    for test_case in xrange(1, t + 1):
        first_answer = int(raw_input()) - 1
        first_grid = [map(int, raw_input().split()) for x in xrange(4)]

        second_answer = int(raw_input()) - 1
        second_grid = [map(int, raw_input().split()) for x in xrange(4)]

        possible_numbers = set(first_grid[first_answer]) & \
                           set(second_grid[second_answer])

        print "Case #%d:" % test_case, solution(possible_numbers)

if __name__ == "__main__":
    main()

