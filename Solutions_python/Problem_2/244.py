import sys
import time

verbose = False
#iFName = sys.argv[1]
iFName = "d:\projekty\google-jam\\train\\B-large.in"

AVAILABLE = False
NEEDED = True
ASTATION = 0
BSTATION = 1

class trainInfo:
    stationName = ['A', 'B']
    def __init__ (self, t, s, a):
        self.time = t
        self.station = s
        self.status = a
    def __str__ (self):
        import operator
        ret = str (self.time) + ' (' + str(operator.div(self.time, 60)) + ':' + str(self.time % 60) + ') ' + \
              self.stationName[self.station] + ' '
        if self.status ==  AVAILABLE:
            ret = ret + "AVAIL"
        else:
            ret = ret + "NEED"
        return ret
    
#key function for sorting    
def tiKey (ti):
    return ti.time

def tiCmp (a, b):
    if a.time < b.time:
        return -1
    if a.time > b.time:
        return 1
    #here a.time = b.time
    if a.status < b.status :
        return -1
    if a.status > b.status :
        return 1    
    return 0

def readDta (f, cnt, src, dst, taTime):
    events = []
    for j in range (cnt):
        L = f.readline()
        if verbose:
            print L
        L = L.split()
        Lt = L[0].split(":")
        if verbose:
            print "L ", L, "Lt ", Lt        
        events.append(trainInfo(int(Lt[0]) * 60 + int(Lt[1]), src, NEEDED))
        Lt = L[1].split(":")
        if verbose:
            print "L ", L, "Lt ", Lt        
        events.append(trainInfo(int(Lt[0]) * 60 + int(Lt[1]) + taTime, dst, AVAILABLE))
    return events

if verbose:
    print "Input file: ", iFName
iFile = open(iFName, "r")
#how many cases?
N = int( iFile.readline())
for i in range(N) :
    #read turnaround time
    T = int( iFile.readline())
    #read NA ad NB
    L = iFile.readline()
    if verbose:
        print "T ", T
        print "L ", L
    NA = int (L.split()[0])
    NB = int (L.split()[1])
    if verbose:
        print "NA ", NA
        print "NB ", NB
    #read departure and arrival times and convert them to events
    events = readDta (iFile, NA, ASTATION, BSTATION, T) +  readDta (iFile, NB, BSTATION, ASTATION, T)
    if verbose:
        for e in events:
            print e
    #sort event asc according to time
    events.sort (cmp=tiCmp)
    if verbose:
        print "SORTED"
        for e in events:
            print e    
    #compute number of trains needed
    initial = [0, 0]
    current = [0, 0]
    for e in events:
        if e.status == AVAILABLE :
           current[e.station] = current[e.station] + 1
        else:
            if current[e.station] > 0 :
                current[e.station] = current[e.station] - 1
            else:
                initial[e.station] = initial [e.station] + 1
        
    print "Case #%(i)d: %(ta)d %(tb)d" % {'i' : i + 1, 'ta' : initial[ASTATION], 'tb' : initial[BSTATION]}
iFile.close()
