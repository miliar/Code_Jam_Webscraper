def worldcup(preferences, depth, prices):
    # Match pyramid.
    watched = [ [False] * (2**i) for i in range(0,depth) ]
    price = 0

    # For each team
    for team, matches in enumerate(preferences):
        # If we already have watched enough matches, ignore.
        #print "Team", team, matches
        if matches >= depth:
            continue

        # Start at the root, and for each level...
        #print watched
        #print "To go: ", (depth-matches)
        for level in xrange(depth):
            #print "Level ", level
            # If we have not watched the match at this level...
            match = team / (2**(depth-level))
            #print team, (depth-level), match
            if not watched[level][match]:
                # Watch it, and add one to the matches of all teams possibly playing.
                watched[level][match] = True
                #print watched
                price += 1
                #print preferences
                for coteam in range(match * 2**(depth-level), (match+1) * 2**(depth-level)):
                    preferences[coteam] += 1
                #print preferences
            if preferences[team] >= depth:
                break
    return price

def main():
    cases = int(raw_input())
    for case in xrange(cases):
        depth = int(raw_input())
        preferences = map(int, raw_input().split(" "))
        prices = [None]*depth
        for level in range(depth)[::-1]:
            prices[level] = map(int, raw_input().split(" "))
        print "Case #%d: %d" % (case+1, worldcup(preferences, depth, prices))

main()
