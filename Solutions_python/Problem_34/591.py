#!/usr/bin/env python

def main():
  """Read the input"""
  file = "A-large.in"
  f = open(file)
  data = f.readline()
  L, D, N = map(int, data.split(" "))
  words = []
  for i in range(D):
    words.append(f.readline().replace('\n', ''))
  groups = {}
  count = 1
  f2 = open("output.txt", 'w')
  for i in range(N):
    group = f.readline().replace('\n', '')
    areas = get_combos(group)
    matches = 0
    for word in words:
      match = True
      for i in range(L):
        if word[i] not in areas[i + 1]:
          match = False
      if match:
        matches += 1
    f2.write("Case #%d: %d\n" % (count, matches))
    count += 1
  f2.close()

def get_combos(pattern):
  in_area = False
  area_count = 0
  areas = {}
  for i in range(len(pattern)):
    if pattern[i] == '(':
      in_area = True
      area_count += 1
    elif pattern[i] == ')':
      in_area = False
    else:
      if in_area:
        if area_count not in areas:
          areas[area_count] = pattern[i]
        else:
          areas[area_count] += pattern[i]
      else:
        area_count += 1
        areas[area_count] = pattern[i]
  return areas

if __name__ == "__main__": main()
