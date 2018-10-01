import sys
import numpy as np
#import math


infilepath, outfilepath = sys.argv[1], sys.argv[2]

def check_is_tidy(number):
  num_string = str(number)
  if len(num_string) == 1:
    return True
  for i in range(len(num_string) - 1):
    if int(num_string[i]) > int(num_string[i + 1]):
      return False
  return True

lines = None
output_lines = []
with open(infilepath) as infile:
  lines = infile.readlines()[1:]

i = 1

for line in lines:
  current_number = long(line)
  if check_is_tidy(current_number):
    output_lines.append('Case #' + str(i) + ': ' + str(current_number) + '\n')
    i += 1
    continue
  else:
    # total_powers_ten = math.log10(current_number)
    current_power_10 = 1
    while not check_is_tidy(current_number):
      subtractor = current_number % (10 ** current_power_10) + 1
      current_number -= subtractor
      current_power_10 += 1
    output_lines.append('Case #' + str(i) + ': ' + str(current_number) + '\n')
    i += 1



with open(outfilepath, 'w') as outfile:
  outfile.writelines(output_lines)