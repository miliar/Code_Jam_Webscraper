import math

from math import sqrt

def is_palendrome_bool(num):
  return is_palendrome(num) == num

def is_palendrome(n, partial=0):
    if n == 0:
        return partial
    return is_palendrome(n / 10, partial * 10 + n % 10)

def print_fair_and_squares_for_range(case, bot, top, o):
  bot_range = int(math.sqrt(bot))
  top_range = int(math.sqrt(top)) + 1
  
  count = 0
  
  for x in range(bot_range, top_range):
    squared = x*x
    if ((squared >= bot) & (squared <= top)):
      #check if both squared and x is a palendrome
      #if yes, then increment count
      if (is_palendrome_bool(x) & is_palendrome_bool(squared)):
        count += 1
  output = 'Case #' + str(case) + ': ' + str(count) + '\n'
  print output
  o.write(output)

#print_fair_and_squares_for_range(1, 1, 4)
#print_fair_and_squares_for_range(2, 10, 120)
#print_fair_and_squares_for_range(3, 100, 1000

f = open('fairandsquare.in')
o = open('fairandsquare.out','r+')
num_cases = int(f.readline()) + 1
for case in range(1, num_cases):
  r = f.readline().rsplit()
  print_fair_and_squares_for_range(case,  int(r[0]), int(r[1]), o)

#r = f.readline().rsplit()



#def is_fair_and_square(num): 

#print is_fair_and_square(121)
#print is_fair_and_square(9)
#print is_fair_and_square(1)
#print is_fair_and_square(16)
#print is_fair_and_square(22)
#print is_fair_and_square(676)
#print is_palendrome_bool(11)
#print is_palendrome_bool(13321)
#print is_palendrome_bool(12321)
#print is_palendrome_bool(123210)
#print is_palendrome_bool(0123210)
