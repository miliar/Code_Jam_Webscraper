# Rahul Butani
# April 7th, 2017

import math

# Takes N and K as a space separated string.
# Returns max and min for the chosen stall for the Kth person as a space
# separated string, in that order.
def probC(testCase):
	(N, K) = [int(x) for x in testCase.split(' ')]
	
	# First find the highest integer value of a for which (2^a)-1 <= K is true
	# This is equivalent to floor(log-base-2(K+1))
	ClosestCleanState = int(math.log((K+1), 2))

	# Now find (2^a)-1
	# These values (powers of 2, minus 1) are the values for which we can
	# accurately and quickly compute the length of contiguous sections of
	# empty bathroom stalls
	# Note that the value of ClosestCleanState is the number of people in the
	# stalls at the point in time
	ClosestCleanState = 2**ClosestCleanState - 1

	# At the point in time that CloestCleanState refers to, compute the number
	# of open stalls (simply total stalls - number of people at the time)
	NumOpenSpaces = N - ClosestCleanState

	# The number of open spaces must be distributed in (the number of people 
	# in the stalls + 1) number of chunks
	NumChunks = ClosestCleanState + 1

	# Dividing the number of open stalls by the number of chunks and rounding
	# down gives us the lower possibility for the size of the contiguous
	# chunks
	LowerPossibility = int(NumOpenSpaces/(NumChunks))

	# At a clean state point in time, the length of the contiguous chunks of 
	# empty stalls will only be one or two distinct values; odd or even
	# Adding one to the lower possibility gives us the higher possibility
	HigherPossibility = LowerPossibility + 1

	# HigherPossibilityCount * HigherPossibility + LowerPossibilityCount * 
	# LowerPossiblity must equal NumOpenSpaces and HigherPossibility is one
	# greater than LowerPossibility
	# Therefore the HigherPossibilityCount is equal to the following:
	HigherPossibilityCount = NumOpenSpaces - (NumChunks*LowerPossibility)

	# All the remaining chunks must be of the lower possibility length
	LowerPossibilityCount = NumOpenSpaces - HigherPossibilityCount

	# Now we may need to go forward in time (i.e. add more people to the 
	# stalls) to the point we were actually asked about
	# First we find out how many people we need to add on top of the clean
	# state we calculated for
	StallDwellersToAdd = K - ClosestCleanState

	# If this isn't actually necessary (i.e. we're adding 0 people, we're done
	# here)
	# We already know the minimum number of spaces and so long as
	# HigherPossibilityCount is non-zero, we know the higher number too
	# If HigherPossibilityCount is zero, LowerPossibility is both our min and
	# max
	if StallDwellersToAdd is 0:
		return "{} {}".format(HigherPossibility if HigherPossibilityCount is \
			not 0 else LowerPossibility, LowerPossibility)

	# In order to find the min/max number of stalls to the left/right of the
	# stall the last person enters, we need to figure out the size of the 
	# contiguous chunk of empty stalls the person decides to inhabit
	# We really only have two options as explained above: Higher or Lower
	# Possibility
	# As per the rules, people will try to inhabit the larger chunk (more 
	# empty spaces) first, so let's see if we have enough of the higher spaces
	# If not, they'll be invading a lower possibility size chunk:
	ChunkToInhabit = HigherPossibility if StallDwellersToAdd <= \
		HigherPossibilityCount else LowerPossibility

	# Now that we have the size of the chunk the last person will be entering
	# we can find the min and max spaces to the left/right pretty easily:
	MinSpaces = int((ChunkToInhabit - 1)/2)
	MaxSpaces = ((ChunkToInhabit - 1) - MinSpaces)

	# Finally return the answer, properly formatted:
	return "{} {}".format(MaxSpaces, MinSpaces)

testCases = list()

with open('C-small-1-attempt0.in', 'r', encoding='utf-8') as input:
	numCases = int(input.readline());
	print("Found {} cases.".format(numCases))

	for i in range(numCases):
		testCases.append(input.readline())

with open('probC_Sol.txt', 'w') as output:
	count = 0
	for test in testCases:
		count += 1

		out = "Case #{}: {}\n".format(count, probC(test))
		
		print(out)
		output.write(out)
