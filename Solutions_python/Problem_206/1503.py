t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  miles,horses = [int(k) for k in input().split(" ")]
  L = []
  for j in range(0,horses):
    distance,speed = [int(k) for k in input().split(" ")]
    hour = (miles-distance)/speed
    L.append(hour)
  max_t = max(L)
  speed = miles/max_t
  print("Case #{}: {:.6f}".format(i,speed))
  # check out .format's specification for more formatting options
