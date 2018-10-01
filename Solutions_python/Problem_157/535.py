import sys

inp = iter(sys.stdin.read().splitlines())
test_cases = int(inp.next().strip('\n'))

def test(case_num, case):
  s_max, s_levels = case.split(" ")
  s_levels = [int(i) for i in s_levels]

  # need to count zeros.
  people_needed = 0
  people_so_far = 0
  for i, level in enumerate(s_levels):
    if people_so_far < i:
      extra_people = i-people_so_far
      people_needed += extra_people
      people_so_far += extra_people

    people_so_far += level
    
  print "Case #%i:" % case_num, people_needed

count = 1
for test_case in inp:

  test(count, test_case)
  count += 1