def solution(D, N, horses):
    max_time = 0
    for k, s in horses:
        dist_left = D - k
        time = dist_left / s
        if time > max_time:
            max_time = time 
    return D/max_time




# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
total = int(input())  # read a line with a single integer
for i in range(1, total + 1):
  D, N = input().split(" ")  # read a list of integers, 2 in this case
  horses = []
  for h_in in range(int(N)):
    k, s = input().split(" ")
    horses.append((int(k),int(s)))

  result = solution(int(D), int(N), horses)
  print("Case #{}: {}".format(i, result))
  # check out .format's specificatin for more formatting options
