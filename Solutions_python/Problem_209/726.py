from math import pi
def solve(radiiHeights,k):
    radii =[]
    heights=[]
    for radh in radiiHeights:
        radii.append(radh[0])
        heights.append(radh[1])
    
    dp= [[0 for i in xrange(k)] for rad in radii]
    
    #initial
    for i in xrange(len(radii)):
        dp[i][0]= pi*radii[i]**2 + 2*pi*radii[i]*heights[i]
    
    #print 'dp',dp[0][0],dp[1][0]
    
    for i in xrange(1,k):
        for rad in xrange(len(radii)):
            maxi=0
            for r in xrange(rad):
                maxi=max(maxi, (dp[r][i-1] + pi*(radii[rad]**2 - radii[r]**2)+2*pi*radii[rad]*heights[rad]) )
            dp[rad][i]=maxi
    return max([dp[rad][k-1] for rad in xrange(len(radii))])
T = input()
for i in xrange(T):
    N,K = map(int,raw_input().split())
    #radii= []
    #heights=[]
    radiiHeights = []
    for j in xrange(N):
        rad,height = map(int,raw_input().split())
        #radii.append(rad)
        #heights.append(height)
        radiiHeights.append((rad,height))
    radiiHeights.sort()
    #print radiiHeights
    soln = solve(radiiHeights,K)
    print "Case #%i: %.7f"%(i+1,soln)
    