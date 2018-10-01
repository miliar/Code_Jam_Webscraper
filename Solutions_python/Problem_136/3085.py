import sys

sys.setrecursionlimit(10000)

def problem_instances(filename):
    f = open(filename)
    num_instances = int(f.readline())
    for i in range(num_instances):
        # Default just returns the line, implement parsing here
        yield map(float, f.readline().split())


def get_time_iter(farm_price, rate_inc, goal):
    current_rate = 2
    elapsed_time = 0

    while True:
        upper_bound = elapsed_time + max(0, goal) / current_rate  # sit and wait from now on
        time_til_next_farm = max(0, farm_price) / current_rate

        current_rate += rate_inc
        rest_time_with_higher_rate = elapsed_time + time_til_next_farm + goal / current_rate

        if rest_time_with_higher_rate >= upper_bound:
            return upper_bound

        elapsed_time += time_til_next_farm


def solve(instance):
    farm_price, rate_inc, goal = instance
    return "%.7f" % get_time_iter(farm_price, rate_inc, goal)


filename = sys.argv[1]
out = open(filename + ".out", "w")
for idx, instance in enumerate(problem_instances(filename), 1):
    out.write("Case #%i: %s\n" % (idx, solve(instance)))