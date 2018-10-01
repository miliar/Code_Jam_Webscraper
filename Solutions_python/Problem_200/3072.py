def last_tidy_number(s):
  """s is a string representing a number."""
  nums = [int(ch) for ch in s]
  num_digits = len(nums)
  cur_min = nums[-1]
  drop_id = num_digits
  for i in range(num_digits - 1, -1, -1):
    if nums[i] > cur_min:
      cur_min = nums[i] - 1
      drop_id = i
    else:
      cur_min = nums[i]
  if drop_id == num_digits:
    return "".join(map(str, nums))
  outputs = nums[:drop_id] + [nums[drop_id] - 1] + [9] * (num_digits - drop_id - 1)
  if outputs[0] == 0:
    return "".join(map(str, outputs[1:]))
  return "".join(map(str, outputs))


num_tests = int(input())
for test_id in range(1, num_tests + 1):
  s = input()
  output = last_tidy_number(s)
  print("Case #{0}: {1}".format(test_id, output))
