vowels = ['a', 'e', 'i', 'o', 'u']

def solve_case(case):
  name = case[0].lower()
  minimum = int(case[1])
    
  substrings = []
  
  result = 0
  
  for start in range(len(name)):
    for end in range(start, len(name)):
      substrings.append(name[start:end + 1])
  
  for substring in substrings:
    consecutive = 0
    for char in substring:
      if char not in vowels:
        consecutive += 1
      else:
        consecutive = 0
      if consecutive >= minimum:
        result += 1
        break
    
  return result

input_file = open('input.in', 'r')
lines = input_file.readlines()
cases = int(lines[0])
lines = lines[1:]
output_string = ""
for i in range(len(lines)):
  output_string += "Case #" + str(i + 1) + ": " + str(solve_case(lines[i].split(' '))) + "\n"

output_file = open('output.out', 'w+b')
output_file.write(output_string)