from math import floor, sqrt

lines = []
with open('input.txt','r') as f:
   lines = f.read().splitlines()

lines.pop(0)
range_list = []
for line in lines:
   line = line.strip().split(' ')
   this_range = (int(line[0]), int(line[1]))
   range_list.append(this_range)

# Credits:
# http://www.johndcook.com/blog/2008/11/17/fast-way-to-test-whether-a-number-is-a-square/
def is_square_of_palindrome(n):

   h = n & 0xF

   if (h > 9):
      return False

   if (h != 2 and h != 3 and h != 5 and h != 6 and h != 8):
      t = int(floor(sqrt(n) + 0.5))
      return ((t*t == n) and is_palindrome(t))

   return False

def is_palindrome(number):
   num_str = str(number)
   return (num_str == num_str[::-1])

def check_range(start_num, end_num):
   #print 'Checking range from %d to %d' % (start_num, end_num)
   count = 0
   for i in range(start_num, end_num + 1):
      if is_palindrome(i) and is_square_of_palindrome(i):
         count += 1
   return count

out_file = open('output.txt','w')

case_num = 1
for r in range_list:
   line = "Case #{}: {}".format(case_num, check_range(r[0], r[1]))
   print(line)
   out_file.write(line + '\n')
   case_num += 1

out_file.close()
