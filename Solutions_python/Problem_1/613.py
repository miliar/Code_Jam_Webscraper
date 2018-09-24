import math
import copy

def searchlist (thelist, thestring):
    length = len(thelist)
    result = -1
    for i in range(length):
        if thelist[i]== thestring:
            result = i
            break
    return result

f=open('A-large.in')
out = open('serveroutput.txt','w')
casemax = int(f.readline())
for i in range(casemax):
    numS = int(f.readline())
    track =[]
    server = []
    for j in range(numS):
        ServerName =f.readline()
        server.append(ServerName)
        track.append(ServerName)
#    print 'server2 and server are'
#    print server2
#    print server
    numQ = int(f.readline())
    #if i ==0:
        #print 'the numQ is'
        #print numQ
    numSwitch = 0
    for k in range(numQ):
        querie = f.readline()
        if i == 0:
            print querie
        pos = searchlist(track, querie)
        if pos > -1:            
            track[pos:pos+1]=[]
        if track == []:
            numSwitch = numSwitch + 1
            track = copy.deepcopy(server)
            pos = searchlist(track,querie)
            track[pos:pos+1]=[]
    out.write('Case #'+str(i+1)+": "+ str(numSwitch)+"\n")
    print 'server is'
    print server
    print 'numswitch is'
    print numSwitch
