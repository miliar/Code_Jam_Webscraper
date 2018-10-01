from math import ceil
from math import floor
from math import log

for tc in range(input()):
  stalls, people = raw_input().split(" ")
  stalls = int(stalls)
  people = int(people)
  to_divide = float(2 ** floor(log(people, 2)))
  divisor, remainder = floor((stalls - to_divide + 1) / to_divide), (stalls - to_divide + 1) % to_divide
  if people - to_divide + 1 <= remainder:
    small, big = floor(divisor * 0.5), ceil(divisor * 0.5)
  else:
    small, big = floor((divisor - 1) * 0.5), ceil((divisor - 1) * 0.5)
  print "Case #" + str(tc + 1) + ": " + str(int(big)) + " " + str(int(small))