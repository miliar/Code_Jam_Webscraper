#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
# author Ladislav Vrbsky
# Google Code Jam 2017
# Qualification round
# Problem A.

def cook(pancakes, k):
  no_pancakes = len(pancakes)
  no_flips = 0
  flips = [0]*(no_pancakes-k+1)
  for ip in range(0,no_pancakes):
    if ip <= no_pancakes-k and not positive(pancakes, ip, flips, k):
      #make a flip
      flips[ip]=1
      no_flips+=1

  for ip in range(1,k):
    if not positive(pancakes, no_pancakes-ip, flips, k):
      return 'IMPOSSIBLE'
  return no_flips

def positive(pancakes, i, flips, k):
  init = 1
  if pancakes[i]=='+':
    init = 0
  no_fliped_before=sum(flips[max(0,i-(k-1)):i])
  #print(flips)
#  print(i, init, no_fliped_before, (init+no_fliped_before) % 2 == 0, i-(k-1))
#   print(i, flips, max(0,i-(k-1)))
  return (init+no_fliped_before) % 2 == 0

def main():
  t = int(input())  # read a line with a single integer
  for i in range(1, t + 1):
    pancakes,k = [inp for inp in input().split(" ")]  # read a list of integers, 2 in this case
    k = int(k)
    print("Case #{}: {}".format(i, cook(pancakes, k)))

if __name__ == '__main__':
  main()