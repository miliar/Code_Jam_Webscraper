def run():
  test_case_count = int(raw_input())  # read a line with a single integer
  for i in range(1, test_case_count + 1):
    state_str, flip_size_str = raw_input().split(" ")
    flip_size = int(flip_size_str)
    state = [ch == '+' for ch in state_str]

    solvable = steps_to_solve(state, flip_size)

    print("Case #{}: {}".format(i, solvable if solvable >= 0 else "IMPOSSIBLE"))

def steps_to_solve(start_state, flip_size):
  steps_taken = 0
  cur_state = list(start_state)

  for idx in range(len(start_state)):
    is_good = cur_state[idx]
    # print is_good, idx
    if idx > len(start_state) - flip_size:
      break
    if not is_good:
      steps_taken += 1
      cur_state = flip(cur_state, idx, flip_size)

  if all(cur_state):
    return steps_taken
  else:
    return -1

def flip(start_state, start_idx, flip_size):
  # print start_state, start_idx, flip_size
  return [not x if start_idx <= idx < (start_idx + flip_size) else x
      for idx, x in enumerate(start_state)]

run()
