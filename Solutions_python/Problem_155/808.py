
in_name = 'A-large.in'
out_name = 'out.txt'

def main():
  infd = open(in_name)
  outfd = open(out_name, 'w')
  T = int(infd.readline())
  for case in range(1, T+1):
    outfd.write('Case #' + str(case) + ': ')
    outfd.write(str(solve(infd.readline())) + '\n')
  infd.close()
  outfd.close()

def solve(line):
  ls = line.split()
  max_shy = int(ls[0])
  shy_str = ls[1]
  add = 0
  num_standing = 0
  for shy_level in range(len(shy_str)):
    if num_standing < shy_level:
      add += shy_level - num_standing
      num_standing = shy_level
    new_people_standing = int(shy_str[shy_level])
    num_standing += new_people_standing
  return add

main()
