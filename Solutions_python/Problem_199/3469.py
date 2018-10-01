def process(start, step, array):
  for i in range(start, start+step):
    if array[i] == '-':
      return i
  return start+step

def flip(start, step, array):
  for i in range(start, start+step):
    array[i] = flipProcess(array[i])

def flipProcess(number):
  if number == '+':
    return '-'
  else:
    return '+'
def check(array, i):
  for j in range(i, len(array)):
    print(array[j])
    if (array[j] == '-'):
      return False
  return True  
def doIt(array, step):
  init = 0
  count = 0
  while init < (len(array) - step + 1):
    print(array)
    print(check(array, init))
    if (array[init] == '-'):
      count = count + 1
      flip(init, step, array)
      init = process(init, step, array) 
    else:
      init = process(init, step, array)
  print(init)
  print(array)
  print('\n')
  print(check(array, init))
  if (init < len(array)) and (check(array, init) == False):
    return -1
  else:
    return count
import sys
#testcase = sys.stdin.readlines()
#print(testcase)

with open(sys.argv[1]) as f:
  testcase = f.readlines()
testcase = [line.rstrip('\n') for line in testcase]
num = int(testcase[0])
result_array = []
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
#t = int(raw_input())  # read a line with a single integer
for i in range(1, num + 1):
  input = testcase[i].strip().split()
  array = list(input[0]) 
  step = int(input[1])
  print('TURN : ' + str(i))
  result = doIt(array, step)
  if (result == -1):
    result_array.append('Case #'+ str(i) + ': ' + 'IMPOSSIBLE')
    #sys.stdout.write('Case #'+ str(i) + ': ' + 'IMPOSSIBLE\n')
  else:
    result_array.append('Case #'+ str(i) + ': ' + str(result))
    #sys.stdout.write('Case #'+ str(i) + ': ' + str(result)+'\n')
with open(sys.argv[2], 'w') as fout:
  for i in result_array:
    fout.write(i + '\n')