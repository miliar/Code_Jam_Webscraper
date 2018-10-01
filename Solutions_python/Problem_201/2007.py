import sys
from pprint import pprint

def get_num_input():
  num = sys.stdin.readline()
  try:
    num = int(num)
  except ValueError:
    print("Error : first line of input is not an int")
    exit()
  return num

def line_to_item(line):
  item = line.split(" ")
  item[0] = int(item[0])
  item[1] = int(item[1])
  return item

def empty_on_left(stalls, i):
  count = 0
  while True:
    if i == 0:
      return count
    elif stalls[i-1] == 0:
      count += 1
      i -= 1
    else:
      return count

def empty_on_right(stalls, i):
  count = 0
  while True:
    if i == len(stalls)-1:
      return count
    elif stalls[i+1] == 0:
      count += 1
      i += 1
    else:
      return count

def get_best_pos(stalls):
  best_pos = 0
  best_min = 0
  best_max = 0
  for i in range(1, len(stalls)-1):
    if stalls[i] == 1:
      continue
    else:
      L = empty_on_left(stalls, i)
      R = empty_on_right(stalls, i)
      if min(L, R) > best_min:    #if the cur pos has better min
        best_pos = i                #we've found a new best
        best_min = min(L, R)
        best_max = max(L, R)
      elif min(L, R) == best_min: #if the cur pos has equal min
        if max(L, R) > best_max:  #look at the max, if it's better
          best_pos = i              #we've found a new best
          best_min = min(L, R)
          best_max = max(L, R)
        #if the min and the max are equal, we choose the leftmost pos,
        #which is the one we already have, since we're iterating from
        #left to right
  return best_pos, best_min, best_max
          
      

def compute(item):
  stalls = [0 for i in range(item[0])]
  #add ones to both sides  
  stalls.append(1)
  stalls.reverse()
  stalls.append(1)
  #start looping
  for i in range(item[1]):
    (best_pos, best_min, best_max) = get_best_pos(stalls)
    stalls[best_pos] = 1
  return (best_min, best_max)
      

def main():
  num = get_num_input()
  
  #MAIN LOOP
  i = 0
  for line in sys.stdin:
    i += 1
    print("Case #" + str(i) + ": ", end='')
    item = line_to_item(line)
    (best_min, best_max) = compute(item)
    print(str(best_max) + " " + str(best_min))

main()


  
