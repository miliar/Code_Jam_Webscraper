'''
Created on Apr 10, 2015

@author: JuanFMx2
'''
import sys
import os.path
import traceback
import heapq 
from fractions import gcd

 
# Least common multiple is not in standard libraries? It's in gmpy, but this is simple enough:
 
def lcm(a, b):
  return (a * b) / gcd(a, b)

def get_next_barber(heap_free,heap_busy):
  if len(heap_free) == 0:
    min_time_barb = heapq.heappop(heap_busy)
    heapq.heappush(heap_free,[min_time_barb[2],min_time_barb[1]])
    while len(heap_busy) > 0 and heap_busy[0][0] == min_time_barb[0]:
      min_time_barb = heapq.heappop(heap_busy)
      heapq.heappush(heap_free,[min_time_barb[2],min_time_barb[1]])
    i=0
    while i < len(heap_busy):
      heap_busy[i][0] = heap_busy[i][0]-min_time_barb[0]
      i += 1
  barb = heapq.heappop(heap_free)
  heapq.heappush(heap_busy, [barb[1],barb[1],barb[0]])
  return barb[0]
      

def b_round_1a(case_num,line_input_1,line_input_2):
  answer = None
  try:
    parts = line_input_1.split()
    num_b = int(parts[0])
    my_num = long(parts[1])
    parts = line_input_2.split()
    barbs_heap = []
    barbs_busy_heap = []
    costs = []
    lcm_val = 1
    i = 0
    while i < num_b:
      cost_i = int(parts[i])
      heapq.heappush(barbs_heap, [(i+1),cost_i])
      costs.append(cost_i)
      lcm_val = lcm(lcm_val, cost_i)
      i += 1
    num_clients_repeat = 0
    i = 0
    while i < num_b:
      num_clients_repeat +=  lcm_val/costs[i]
      i+=1
     
    my_num = my_num % num_clients_repeat
    if my_num == 0:
      my_num = num_clients_repeat
    i=0
    while i < my_num:
      answer = get_next_barber(barbs_heap,barbs_busy_heap)
      i+=1
  except:
    traceback.print_exc()
    print "Error parsing line \n%s\n%s"%(line_input_1,line_input_2)
    sys.exit(0)
  print "Case #%s: %s"%(case_num,answer)

def parse_input(input_path, process_test_case_func):
  with open(input_path) as f:
    cur_line = f.readline()
    try:
      num_lines_to_process = int(cur_line)
    except:
      print "'%s' is not a number!" % cur_line
      sys.exit(0)
    
    for i in range(num_lines_to_process):
      line_1 = f.readline()
      if not cur_line:
        print "line %s is empty!" % cur_line
        sys.exit(0)
      line_2 = f.readline()
      if not cur_line:
        print "line %s is empty!" % cur_line
        sys.exit(0)
      process_test_case_func((i+1),line_1,line_2)
    content = f.readlines()

def main(input_path):
  if os.path.isfile(input_path):
    parse_input(input_path,b_round_1a)
  else:
    print "Unknown file: '%s'" % input_path
    sys.exit(0)
    
if __name__ == "__main__":
  if len(sys.argv) >= 2:
    main(sys.argv[1])
  else:
    print "Insufficient Parameters"
    sys.exit(0)