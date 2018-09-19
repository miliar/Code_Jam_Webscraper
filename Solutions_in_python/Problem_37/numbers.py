import sys

MIN_BASE = 2
MAX_BASE = 10
HAPPY_LOOKUP = {}

CURR_LIST = []


def sum(num1, num2, base):
  num1 = '0%s' % num1
  num2 = '0%s' % num2
  out = []
  p1 = len(num1)-1
  p2 = len(num2)-1
  carry = 0
  while max(p1, p2) > 0:
    out.append(str((int(num1[p1]) + int(num2[p2]) + carry) % base))
    carry = (int(num1[p1]) + int(num2[p2]) + carry) // base
    if p1 > 0: 
      p1 -= 1
    if p2 > 0: 
      p2 -= 1
  out.append(str(carry))
  out.reverse()
  return ''.join(out).lstrip('0')  
   
def convert(num, base):
  out = []
  while num > 0:
    out.append(str(num % base))
    num = num // base
  out.reverse()
  return ''.join(out) 


def square(num, base):
  sq = int(num)*int(num)
  return convert(sq, base)


def is_happy(num, base):
  global CURR_LIST, HAPPY_LOOKUP
  if num in HAPPY_LOOKUP[base]:
    CURR_LIST = []
    return HAPPY_LOOKUP[base][num]
  else:
    running_sum = '0'
    for i in range(len(num)):
      char = num[i]
      running_sum = sum(running_sum, square(char, base), base)
    running_sum = running_sum.lstrip('0')
    if running_sum == '1':
      HAPPY_LOOKUP[base][num] = True
      CURR_LIST = []
      return True
    elif running_sum == '' or running_sum in CURR_LIST:
      HAPPY_LOOKUP[base][num] = False
      CURR_LIST = []
      return False
    else:
      CURR_LIST.append(running_sum)
      return is_happy(running_sum, base)

def get_ints(infile):
  return [int(x) for x in infile.readline().strip().split()]


def get_int(infile):
  return int(infile.readline().strip())


def init_data_structures():
  global HAPPY_LOOKUP
  for i in range(MIN_BASE, MAX_BASE+1):
    HAPPY_LOOKUP[i] = {}


def read_case(infile):
  bases = get_ints(infile)
  return bases


def solve_case(data):
  i = 1
  done = False
  while not done:
    i += 1
    done = True
    for base in data:
      if not is_happy(convert(i, base), base):
        done = False
        break
  return i


def print_solution(solution, outfile):
  outfile.write(' %d\n' % solution)


def main():
  if len(sys.argv) < 2:
    infile = sys.stdin
  else:
    infile = open(sys.argv[1], 'r')
    
  outfile = sys.stdout
  
  num_trials = get_int(infile)
  
  init_data_structures()
  for case in range(num_trials):
    data = read_case(infile)
    solution = solve_case(data)
    outfile.write('Case #%d:' % (case+1))
    print_solution(solution, outfile)


if __name__ == '__main__':
  main()