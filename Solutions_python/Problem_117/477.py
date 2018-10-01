#!/usr/bin/python
import sys

def get_heights(table):
  result = {}
  for row in table:
    for item in row:
      result[item] = 1
  return sorted(result.keys())

def check_remain(table, key):
  for row in table:
    for item in row:
      if item == key:
        return True
  return False


def check_line(line, key):
  e = 0
  for item in line:
    if item == key:
      e += 1
  return e

def check(table, key):
#  print 'check init:', table, 'key: ',key

  while(len(table)):
#    print table
    c = 0
    for i in range(len(table)):
      e = check_line(table[i], key) 
#      print 's1', 'i:', i, 'e:', e
      if e == len(table[0]):
        del table[i] 
        c = 1
        break
    if c:
      continue

    for i in range(len(table[0])):
      tmp = [item[i] for item in table ]
      e = check_line(tmp, key)
#      print 's2', 'i:', i, 'e:', e
      if e == len(table):
        for item in table:
          item.pop(i)
        c = 1
        break
    if c:
      continue
    else:
      break
#  print 'final table: ',table

  if check_remain(table, key):
    return None
  else:
    return table

def solve(file_name):

  f = open(file_name)
  cases = int(f.readline())

  for case in range(cases):
    n, m = map(int, f.readline().split())

    lawn = []
    for i in range(n):
      lawn += [ map(int, f.readline().split()) ]
    keys = get_heights(lawn)
    
    for key in keys:
      lawn = check(lawn, key)
      if lawn == None:
        break
    
    if lawn == None:
      ans = 'NO'
    else:
      ans = 'YES'

    print 'Case #{0}: {1}'.format(case+1, ans)

if __name__ == "__main__":

  argvs = sys.argv
  file_name = argvs[1]

  solve(file_name)


