import sys

numTestCases = int(sys.argv[1])

for j in range(0, numTestCases):

    S = sys.argv[3 + 2*j]

    numFriendsToInvite = 0
    sumOfNormalAttendees = 0
    
    for i in range(1, len(S)):
        sumOfNormalAttendees += int(S[i-1])
        if ( sumOfNormalAttendees + numFriendsToInvite ) < i:
            numFriendsToInvite += i - (sumOfNormalAttendees + numFriendsToInvite)
            
    print("Case #{0}: {1}".format(j+1, numFriendsToInvite))