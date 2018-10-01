def run():
  test_case_count = int(raw_input())  # read a line with a single integer
  for case in range(1, test_case_count + 1):
    kilometers, horse_count = [int(x.strip()) for x in raw_input().split(" ")]

    horses = []
    for horse in range(horse_count):
      horses.append(int(x.strip()) for x in raw_input().split(" "))

    solution = solve(kilometers, horses)

    print("Case #{}: {}".format(case, solution))

def solve(dist, horses):
  max_hours = max((1.0 * dist - start_pos) / speed for start_pos, speed in horses)
  return 1.0 * dist / max_hours

run()
