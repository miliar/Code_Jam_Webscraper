import sys
     
def gcd(a,b):
    while b:      
        a, b = b, a % b
    return a
     
numcases = int(sys.stdin.readline())
for casenumber in xrange(1,numcases+1):
    line = sys.stdin.readline().rstrip("\r\n")
    line_elems = line.split(" ")
    max_games_played_today = int( line_elems[0] )
    claimed_percent_won_today = int( line_elems[1] )
    claimed_percent_won_ever = int( line_elems[2] )
    
    result = "Possible"
    
    min_games_played_today_for_pct = 100 / gcd(claimed_percent_won_today, 100)
    if max_games_played_today < min_games_played_today_for_pct:
        result = "Broken"
        
    if claimed_percent_won_ever == 100 and claimed_percent_won_today < 100:
        result = "Broken"
        
    if claimed_percent_won_ever == 0 and claimed_percent_won_today > 0:
        result = "Broken"                


    print "Case #%d: %s" % (casenumber, result)



