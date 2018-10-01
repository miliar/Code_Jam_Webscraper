import sys
import os, stat
import itertools

def main():
    mode = os.fstat(0).st_mode
    input = None
    if stat.S_ISFIFO(mode):
        #print "stdin is piped"
        input = open("input.txt")
    elif stat.S_ISREG(mode):
        #print "stdin is redirected"
        input = sys.stdin
    else:
        #print "stdin is terminal"
        input = open("input.txt")

    numCases = int(input.readline().rstrip('\n'))
    numRows = 2;
    count = 0
    for i in range(numCases):
        firstLine = input.readline().rstrip('\n')
        #secondLine = input.readline().rstrip('\n')
        #numRows = int(firstLine.partition(' ')[0])
        #numCols = int(firstLine.partition(' ')[2])
        # lines = [input.readline().rstrip('\n') for j in range(numRows)]
        [n, c, m] = [int(num) for num in firstLine.split(' ')]
        #sizes = [int(num) for num in secondLine.split(' ')]

        extraLines = [input.readline().rstrip('\n') for j in range(m)]
        #count += numRows + 1

        tickets = []
        for line in extraLines:
            tickets.append([int(num) for num in line.split(' ')])
        #print 'Case #%d:\n%s'%(i+1, '\n'.join(evaluate(lines, numRows, numCols)))
        print 'Case #%d: %s'%(i+1, evaluate(n, c, m, tickets))
    # numLines = int(input.readline())
    # lines = [input.readline().rstrip('\n') for i in range(numLines)]
    # for (i,line) in enumerate(lines):
    #     print 'Case #%d: %s'%(i+1, str(evaluate(line)))

def csplit(line, separator):
    for part in line.split(separator):
        try:
            yield int(part)
        except:
            yield str(part)

def divUp(a, b):
    return a/b + (1 if a%b != 0 else 0)

def evaluate(numSeats, numCustomers, numTickets, tickets):
    customersToSeats = []
    for i in range((numCustomers+1)):
        customersToSeats.append([])
    for ticket in tickets:
        [seat, customer] = ticket
        customersToSeats[customer].append(seat)

    customersToSeats.sort(key=(lambda x: len(x)), reverse=True)

    numRides = len(customersToSeats[0])
    seatsAvailable = []
    seatsUnoccupied = []
    seatRequests = []
    for i in range(numSeats+1):
        seatsAvailable.append(numRides)
        seatsUnoccupied.append(True)
        seatRequests.append(0)

    for i, customerSeats in enumerate(customersToSeats):
        newCustomerSeats = []
        for seat in customerSeats:
            if seatsAvailable[seat] > 0:
                seatsAvailable[seat] -= 1
            else:
                seatRequests[seat] += 1
                seatsUnoccupied[seat] = False
        customersToSeats[i] = newCustomerSeats

    numPromotions = 0
    for seat, numRequests in enumerate(seatRequests):
        if (seatsAvailable[seat] >= numRequests):
            seatsAvailable[seat] -= numRequests
            numRequests = 0
            continue
        else:
            numRequests -= seatsAvailable[seat]
            seatsAvailable[seat] = 0
        isGood = False
        for i in range(1, seat):
            if seatsAvailable[i] > 0:
                if seatsAvailable[i] > numRequests:
                    seatsAvailable[i] -= numRequests
                    numPromotions += numRequests
                    numRequests = 0
                    isGood = True
                    break
                else:
                    numRequests -= seatsAvailable[i]
                    numPromotions += seatsAvailable[i]
                    seatsAvailable[i] = 0
        if not isGood:
            extraRides = numRequests/seat
            numRequests -=  extraRides*seat
            numPromotions += extraRides*(seat-1)
            for i in range(seat+1,len(seatsAvailable)):
                seatsAvailable[i] += extraRides
            numRides += extraRides
            if (numRequests > 0):
                numRides += 1
                for i in range(1,len(seatsAvailable)):
                    seatsAvailable[i] += 1
                numPromotions += numRequests - 1
                for i in range(1,numRequests):
                    seatsAvailable[i] -= 1
                seatsAvailable[seat] -= 1

    return str(numRides) + ' ' + str(numPromotions)

main()

