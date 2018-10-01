import sys

def main():
    # read in command-line arguments
    junk, testFile = sys.argv
    
    data = open(testFile,'r').read().splitlines()
    
    N = int(data[0])
    caseNum = 1
    line = 1
    while line < len(data):
        # turnaround time
        T = int(data[line])
        line += 1
        
        # number of trips
        nTrips = map(int, data[line].split())
        line += 1
    
        # record trip times
        departures = [[],[]]
        arrivals = [[],[]]
        for i in xrange(line,line+nTrips[0]):
            trip = data[i].split()
            departures[0].append(toMinutes(trip[0]))
            arrivals[1].append(toMinutes(trip[1]))
        line += nTrips[0]

        for i in xrange(line,line+nTrips[1]):
            trip = data[i].split()
            departures[1].append(toMinutes(trip[0]))
            arrivals[0].append(toMinutes(trip[1]))
        line += nTrips[1]
    
        # get down to business
        send = [[0] * 60 * 24, [0] * 60 * 24]
        aReady = [0] * 60 * 24
        bReady = [0] * 60 * 24
        
        # populate some useful data structures
        for x in departures[0]:
            send[0][x] += 1
        for x in departures[1]:
            send[1][x] += 1
        for x in arrivals[0]:
            try:
                aReady[x + T] += 1
            except IndexError:
                pass
        for x in arrivals[1]:
            try:
                bReady[x + T] += 1
            except IndexError:
                pass
        
        # simulate the day
        initial = [0,0]
        current = [0,0]
        for t in xrange(60*24):
            current[0] += aReady[t]
            current[1] += bReady[t]
            for dir in [0,1]:
                if send[dir][t] > current[dir]:
                    short = send[dir][t] - current[dir]
                    initial[dir] += short
                    current[dir] += short
                current[dir] -= send[dir][t]
        
        print('Case #' + str(caseNum) + ': ' + str(initial[0]) + " " + str(initial[1]))
        caseNum += 1

def toMinutes(timeStr):
    l = timeStr.split(":")
    return int(l[0]) * 60 + int(l[1])
    
if __name__ == "__main__":
    main()
