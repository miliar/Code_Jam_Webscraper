def get_correct_output(case_number, case_answer):
  print("Case #{}: {}".format(case_number, case_answer))

def is_tidy(nums):
  for i, n in enumerate(nums[:-1]):
    if nums[i] > nums[i+1]:
      return False
  return True

def decrease_by_one(nums):
  new_nums = [0 for _ in nums]
  len_nums = len(nums)
  to_remember = 0
  for i in reversed(range(len_nums)):
    if nums[i] == 0 and i == len_nums-1:
      nums[i] = 9
      to_remember = 1
    elif nums[i] != 0 and i == len_nums-1:
      nums[i] = nums[i] - 1
      to_remember = 0
    elif nums[i] == 0 and to_remember > 0:
      nums[i] = 9
      to_remember = 1
    elif nums[i] != 0 and to_remember > 0:
      nums[i] = nums[i] - to_remember
      to_remember = 0
    else:
      nums[i] = nums[i]
  # delete leading zero if any
  if nums[0] == 0:
    return nums[1:]
  return nums

def get_monotonicy_change_index(nums):
  for i in range(len(nums[:-1])):
    if nums[i] > nums[i+1]:
      return i
  return -1

def set_zero_from_index(nums, index):
  for i in range(index+1, len(nums)):
    nums[i] = 0


def solve_test_case(str_num):
  nums = [int(s) for s in list(str_num)]
  if is_tidy(nums):
    return "".join([str(i) for i in nums])
  while True:
    mc_index = get_monotonicy_change_index(nums)
    if mc_index == -1:
      break
    set_zero_from_index(nums, mc_index)
    nums = decrease_by_one(nums)
  return "".join([str(n) for n in nums])


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  entered_number = str(input())
  test_case_answer = solve_test_case(entered_number)
  get_correct_output(case_number = i, case_answer = test_case_answer)