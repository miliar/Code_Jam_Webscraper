def read_case():
  c, f, x = map(float, raw_input().split())
  return c, f, x


def solve_case(c, f, target):
  current_rate = 2
  time_spent = 0

  while(True):
    time_not_buy = calc_time(current_rate, target, time_spent)
    time_before_buy = calc_time(current_rate, c, time_spent)
    time_after_buy = calc_time(current_rate + f, target, time_before_buy)
    if time_not_buy < time_after_buy:
      return time_not_buy
    time_spent = time_before_buy
    current_rate += f


def calc_time(rate, target, spent_time):
  time = target / rate
  return time + spent_time


def read_and_solve():
  number_of_cases = int(raw_input())
  for case_number in range(1, number_of_cases + 1):
    data = read_case()
    answer = solve_case(*data)
    print 'Case #%d: %s' % (case_number, answer)

if __name__ == '__main__':
  read_and_solve()
