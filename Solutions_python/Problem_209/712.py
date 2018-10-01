import math

def calc_sa(R, H, N):
    #print"calc_sa:"
    #printR
    #printH
    #printN
    area = 0.0
    for i in reversed(range(N)):
        area += R[i]*H[i]
        # if i > 0:
        #     if R[i-1] < R[i]:
        #         area += (R[i]**2 - R[i-1]**2)/2.0
    area += (R[-1]**2)/2.0

    #printarea*2*math.pi
    return area

def solve(N, K, R, H):
    # Create list of Ri*Hi
    # Create a list of Ri*Hi + Ri**2/2
    RH = []
    R2RH = []
    
    
    # Sort R, H based on the radius R, and then within that sort by H
    # R, H  = [list(x) for x in zip(*sorted(zip(R, H), key=lambda pair: pair[0]))]
    H = [x for (y,x) in sorted(zip(R,H))]
    R.sort()
    for i in range(N):
        RH.append(R[i]*H[i])
        R2RH.append(R[i]**2/2.0 + R[i]*H[i])

    #printR
    #printH
    #printRH
    #printR2RH

    # Dynamic programming: Get the full stack and then remove area from it!
    # area = 0.0
    # for i in reversed(range(N)):
    #     area += R[i]*H[i]
    #     if i > 0:
    #         if R[i-1] < R[i]:
    #             area += (R[i]**2 - R[i-1]**2)/2
    # area += (R[0]**2)/2
    area = calc_sa(R,H,N)

    # Dynamic programming: remove one pancake at a time
    area_list = [0]*N
    area_list[N-1] = area
    for i in reversed(range(K-1,N-1)):
        #print"i for the size of the cake", i
        #printlen(R)
        area_removed = []
        # Determine which pancake to remove
        
        for j in range(i+2):
            R_temp = R[:]
            H_temp = H[:]
            del R_temp[j]
            del H_temp[j]
            area_removed.append(calc_sa(R_temp, H_temp, i+1))
        
        #print[x*2*math.pi for x in area_removed]
        best_to_remove_index = area_removed.index(max(area_removed)) # Does it matter which one we remove if same area difference?
        del R[best_to_remove_index]
        del H[best_to_remove_index]
        #print"remove index:" , best_to_remove_index
        #printmax(area_removed)*2*math.pi
        area_list[i] = max(area_removed)
    
    return area_list[K-1]*2*math.pi

    # # Dynamic programming 
    # best_area = [R[N-1]*H[N-1]] # Store the largest pancke with largest height first
    # curr_pancake_area = [N-1]
    # # Continue to the second last element
    # for i in range(1,K-1):
    #     # Add the next pancake with the same radius 
    #     option1 = 
    #     best_area[i] 

    # Find max R*H and use it
    

    # Use dynamic programming several times?

    # for i in range(K):
    #     area += R[N-1-i]*H[N-1-i]
    #     if i > 0:
    #         if R[N-1-(i-1)] > R[N-1-i]:
    #             area += R[N-1-(i-1)]**2 - R[N-1-i]**2
    # area += (R[N-1-K+1]**2)/2
    
    # area = area*2*math.pi
    # return area

# The first line of the input gives the number of test cases, T. 
# T test cases follow. 
# Each begins with one line with two integers N and K: 
# the total number of available pancakes, and the size of the stack that the diner has ordered. 
# Then, N more lines follow. Each contains two integers Ri and Hi: the radius and height of the i-th pancake, in millimeters.
T = int(raw_input())  # read a line with a single integer
for tt in xrange(1, T + 1):
    N, K = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    R = []
    H = []
    for i in range(N):
        Ri, Hi = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
        R.append(Ri)
        H.append(Hi)
    ans = solve(N, K, R, H)
    print"Case #{}: {}".format(tt, ans)
    # check out .format's specification for more formatting options