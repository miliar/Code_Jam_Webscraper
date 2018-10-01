import sys

def log(*args, sep=" ", end="\n", file= sys.stderr, flush= False):
    file.write(sep.join(str(a) for a in args) + end)
    if flush:
        file.flush()
    
def getNfriends(maxShy, shy):
    nFriends= 0
    nStanding= 0
    for iLevel, nSitting in zip(range(maxShy + 1), shy):
        nNewFriends= max(0, iLevel - nStanding)
        nFriends += nNewFriends
        nStanding += nSitting + nNewFriends
    return nFriends

if __name__ == "__main__":
    nCases= int(input())
    for iCase in range(1, nCases + 1):
        maxShy, shy= map(str, input().split())
        
        maxShy= int(maxShy)
        shy= list(int(x) for x in shy)
        
        nFriends= getNfriends(maxShy, shy)

        print("Case #{:d}: {:d}".format(iCase, nFriends))