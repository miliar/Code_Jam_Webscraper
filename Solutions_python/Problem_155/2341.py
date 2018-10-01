from __future__ import print_function
from sys import argv

def parse_input(file):
  cases = []
  with open(file) as f:
    for index, line in enumerate(f):
      if index == 0:
        # skip # of cases
        continue

      splitted = line.strip().split(' ')
      cases.append(splitted[1])

  return cases

def calculate_friends_needed(case):
  people_clapping = 0
  friends_needed = 0
  for shyness_level, sitting_people_str in enumerate(case):
    sitting_people = int(sitting_people_str)
    if sitting_people == 0:
      continue

    if people_clapping >= shyness_level:
      people_clapping += sitting_people
    else:
      friends_needed += (shyness_level - people_clapping)
      people_clapping = shyness_level

      people_clapping += sitting_people

  return friends_needed

output = open(argv[2], 'w')

cases = parse_input(argv[1])
for index, case in enumerate(cases):
  friends_needed = calculate_friends_needed(case)

  solution = "Case #{0}: {1}".format(index + 1, friends_needed)
  print(solution)
  print(solution, file=output)


output.close()