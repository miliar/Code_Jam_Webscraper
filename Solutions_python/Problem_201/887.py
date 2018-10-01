import math
T = int(input())
for c in range(T):
  n, k = map(int, input().split(" "))
  num_people = k-1 # before the last person
  divides = math.floor(math.log(num_people+1, 2))
  largest_space = math.ceil((n-num_people)/(2**divides))
  average_LR = (largest_space-1)/2
  mn = math.floor(average_LR)
  mx = math.ceil(average_LR)
  print("Case #{}: {} {}".format(c+1, mx, mn))