def solve_case(cost, farm_rate, goal):
  rate = 2
  time = 0
  while True:
    if (goal < (goal * rate) /  (rate + farm_rate) + cost):
      time += goal / rate
      return time
    elif goal > cost:
      time += cost / rate
      rate += farm_rate

def main():
  case_count = int(raw_input())
  for i in xrange(case_count):
    cost, farm_rate, goal = (float(n) for n in raw_input().split())
    print 'Case #{}: {:.7f}'.format(i+1, solve_case(cost, farm_rate, goal))
  
if __name__ == '__main__':
  main()