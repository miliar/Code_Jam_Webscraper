import pdb

#input_filename = 'sample_input.txt'
input_filename = 'C-small-attempt0.in'
#input_filename = 'C-large.in'
input_file = open(input_filename)
output_file = open(''.join(('output_',input_filename)), 'w')
num_cases = int(input_file.readline())

for case_number in xrange(num_cases):
  line  = input_file.readline()
  runs, seats, num_groups = map(int, line.split())
  group_line = input_file.readline()
  groups = map(int, group_line.split())

  sum = 0
  next_group = 0
  for run in xrange(runs):
    starting = next_group
    # We start off with the all empty seats, minus the first group
    seats_left = seats - groups[next_group]
    sum += groups[next_group]
    next_group += 1
    # If we have reached the end of the list, start over
    if (next_group >= num_groups):
      next_group -= num_groups
    while ((groups[next_group] <= seats_left) and (next_group <> starting)):
      # This group takes a certain number of seats
      seats_left -= groups[next_group]
      # Add what they pay to the sum
      sum += groups[next_group]
      next_group += 1
      # If we have reached the end of the list, start over
      if (next_group >= num_groups):
        next_group -= num_groups

  string = 'Case #' + str(case_number+1) + ': ' + str(sum) + '\n'
  output_file.write(string)

output_file.close()
input_file.close()

