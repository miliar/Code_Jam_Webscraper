from future.builtins import input
import sys

def find_solution(distance, horses):
    max_time = 0
    for x in horses:
        need_time = (distance - x[0]) / float(x[1])
        max_time = max(need_time, max_time)

    return distance / float(max_time)

def test():
    # print("---Start Test---")

    test_cases_in = [
        [2525, [(2400, 5)]],
        [300, [(120, 60), (60, 90)]],
        [100, [(80,100), (70, 10)]],
    ]
    test_cases_out = [
        101.000000,
        100.000000,
        33.333333,
    ]


    for i in range(len(test_cases_in)):
        solution = find_solution(test_cases_in[i][0], test_cases_in[i][1])
        try:
            assert (solution - test_cases_out[i] < 0.000001)
        except:
            print("%d : expected %s, but actual %s" %
                  (i, test_cases_out[i], solution))

    # print("---End Test---")

test()

T = int(input())
for t in range(T):
    distance, num = [int(x) for x in input().split()]
    # print(distance, num)
    position_velocity = []
    for i in range(num):
        position_velocity.append([int(x) for x in input().split()])

    solution = find_solution(distance, position_velocity)
    # print(solution)

    output_text = "Case #{}: {}".format(t + 1, solution)
    print(output_text)
