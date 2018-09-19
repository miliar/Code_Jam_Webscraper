#!/usr/local/bin/python3.0

import sys


def lowestCost(nRounds, maxMisses, ticketPrices):
    assert(nRounds > 0)
    assert( all(0 <= m <= nRounds for m in maxMisses) )
    assert( all( p >= 0 for line in ticketPrices for p in line ) )
    
    # priceForMisses is a list of length 2**roundsLeft.
    # Each element is a list of length roundsLeft+1.
    roundsLeft = nRounds
    priceForMisses = [ [ 0 if i <= m else None
        for i in range(roundsLeft+1) ] 
            for m in maxMisses ]

    while roundsLeft > 0:
        nextPriceForMisses = list()
        
        for match in range(2**(roundsLeft-1)):
            ticketPrice = ticketPrices[0][match]
            costs1 = priceForMisses[2*match]
            costs2 = priceForMisses[2*match+1]
            
            newCosts = [ None for i in range(roundsLeft) ]
            for misses1 in range(roundsLeft+1):
                if costs1[misses1] is not None:
                    for misses2 in range(roundsLeft+1):
                        if costs2[misses2] is not None:
                            misses = min(misses1, misses2)
                            cost = costs1[misses1] + costs2[misses2]
                            if misses > 0 and (newCosts[misses-1] is None
                                    or newCosts[misses-1] > cost):
                               newCosts[misses-1] = cost 
                            if misses < roundsLeft and (newCosts[misses] is None
                                    or newCosts[misses] > cost + ticketPrice):
                               newCosts[misses] = cost + ticketPrice
                    
            nextPriceForMisses.append(newCosts)
        
        priceForMisses = nextPriceForMisses
        roundsLeft -= 1
        ticketPrices = ticketPrices[1:]

    return priceForMisses[0][0]


def getLineOfNumbers(f):
    return [ int(s) for s in next(f).split() ]

def invalidInput():
    sys.exit('Invalid input')


numbers = getLineOfNumbers(sys.stdin)
if len(numbers) != 1:
    invalidInput()

T = numbers[0]

for caseNumber in range(1, T+1):
    numbers = getLineOfNumbers(sys.stdin)
    if len(numbers) != 1:
        invalidInput()
    P = numbers[0]
    
    M = getLineOfNumbers(sys.stdin)
    if len(M) != 2**P:
        invalidInput()
    
    ticketPrices = [ getLineOfNumbers(sys.stdin) for round in range(P) ]
    for round in range(P):
        if len(ticketPrices[round]) != 2**(P-(round+1)):
            invalidInput()

    result = lowestCost(P, M, ticketPrices)
    print( 'Case #{0}: {1}'.format(caseNumber, result) )
