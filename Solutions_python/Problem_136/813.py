import sys

BASE_RATE = 2.0

def optimal_goal_time(farm_price, farm_rate, goal):
    current_time = 0.0
    current_rate = BASE_RATE
    min_goal_time = goal / BASE_RATE
    while min_goal_time > current_time:
        min_goal_time = min(min_goal_time, current_time + goal / current_rate)
        current_time += farm_price / current_rate
        current_rate += farm_rate
    return min_goal_time



def main():
    istream = sys.stdin
    number_of_cases = int(istream.readline())
    for case_no in xrange(1, number_of_cases + 1):
        farm_price, farm_rate, goal = map(float, istream.readline().split())
        print 'Case #%d: %.7f' % (case_no, optimal_goal_time(farm_price, farm_rate, goal))


if __name__ == '__main__':
    main()
