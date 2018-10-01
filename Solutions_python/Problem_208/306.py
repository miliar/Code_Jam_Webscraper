import math

def solve(N, Q, E, S, D, cities):
    # Small dataset
    # Dij = -1, for all i, j where i + 1 =/= j. (The cities are in a single line; each route goes from one city to the next city in line.)
    # Q = 1.
    # U1 = 1.
    # V1 = N. (The only delivery to calculate is between the first and last cities in the line).

    # print N, Q
    # print E
    # print S 
    # print D 
    # print cities

    A = [0] * N # Stores the minimum time from first city to ith city
    for i in range(1,N):
        travel_times = []
        # Calculate the time for horse j to i 
        for j in range(i):
            # Sum the distance from j to i 
            distance = 0
            for k in range(j, i):
                distance += D[k][k+1] 
            # Check if the distance is less than the horse distance
            if E[j] >= distance:
                travel_times.append(float(distance) / S[j]) # Time for that horse j to travel to i 
            else:
                travel_times.append(10**15) # Infinite time
        # Calculate A[j] + travel_times[j]
        new_A = []
        for j in range(i):
            new_A.append(A[j]+travel_times[j])
        A[i] = min(new_A)

    ans = A[N-1]
    return ans

T = int(raw_input())  # read a line with a single integer
for tt in xrange(1, T + 1):
  N, Q = [int(s) for s in raw_input().split(" ")]
  E = []
  S = []
  D = []
  cities = []
  for i in range(N):
      Ei, Si = [int(s) for s in raw_input().split(" ")]
      E.append(Ei)
      S.append(Si)
  for i in range(N):
      row = [int(s) for s in raw_input().split(" ")]
      D.append(row)
  for i in range(Q):
      Uk, Vk = [int(s) for s in raw_input().split(" ")]
      cities.append((Uk,Vk))


  ans = solve(N, Q, E, S, D, cities)
  print "Case #{}: {}".format(tt, ans)