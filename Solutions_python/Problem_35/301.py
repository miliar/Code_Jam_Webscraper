#!/usr/bin/python

import string, sys

height = 0
width = 0
map = []
result = []
next_char = ''

def map_get(p):
   global map
   
   return map[p[0]][p[1]]
   
def result_get(p):
   global result
   
   return result[p[0]][p[1]]

def mark(y, x):
   global map, height, width, next_char, result
   
   lowest_coord = (y, x)
   
   north = (y - 1, x)
   west = (y, x - 1)
   east = (y, x + 1)
   south = (y + 1, x)
   
   if y > 0 and map_get(north) < map_get(lowest_coord):
      lowest_coord = north
      
   if x > 0 and map_get(west) < map_get(lowest_coord):
      lowest_coord = west
      
   if x < width - 1 and map_get(east) < map_get(lowest_coord):
      lowest_coord = east
      
   if y < height - 1 and map_get(south) < map_get(lowest_coord):
      lowest_coord = south
      
   char = ''
   if lowest_coord == (y, x):
      char = next_char
      next_char = chr(ord(next_char) + 1)
   elif result_get(lowest_coord) == ' ':
      char = mark(lowest_coord[0], lowest_coord[1])
   else:
      char = result_get(lowest_coord)
      
   result[y][x] = char
   return char

def case():
   global height, width, result, map
   
   y = 0   
   while y < height:
      x = 0
      while x < width:
         if result[y][x] == ' ':
            mark(y, x)
         
         x += 1
      
      y += 1

def main():
   global map, height, width, next_char, result
   
   f = open(sys.argv[1])
   caseCount = int(f.readline())
	
   for caseNum in range(0, caseCount):
      height, width = [int(x) for x in f.readline().strip().split(" ")]
      
      map = []
      for y in range(0, height):
         row = [int(x) for x in f.readline().strip().split(" ")]
         map += [row]
         
      result = [[' '] * width for i in xrange(height)]
      next_char = 'a'
      
      case()
      
      result = "\n".join([" ".join(line) for line in result])
      print "Case #%d:\n%s" % (caseNum + 1, result)

main()
