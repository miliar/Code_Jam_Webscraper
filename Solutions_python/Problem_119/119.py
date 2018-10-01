
import sys
import string
import math
from math import sqrt
from math import pow
from math import log10

data = sys.stdin.readlines()

nbSamples = int(data.pop(0))
# print "nbSamples: ", nbSamples

currSample = 1

# After x, y, you are in the same situation that y, x
# So, if x, y is bad, so is y, x
badstart = []

def openChest(keyList, chestList, closeChestList, string, current):

#    print "with len ", len(closeChestList)
    
#    print "current", current
#    
#    if len(badstart):
#        print "bad start", badstart[0]
    
    if len(closeChestList) == 0:
        print string
        return 1
    
    if len(keyList) == 0:
        return 0
    
    # Search a key that can open a closed chest

    keylistUniq = set(keyList[:])

    for ch in closeChestList[:]:
        for key in keylistUniq:
    
            if ch.keyToOpen == key:
                # We can try
#                print "trying key", key, " on chest ", ch.index

                newcurrent = current[:]
                newcurrent.append(int(ch.index))
            
                newcurrent.sort()
            
#                if not newcurrent in badstart:
                if 1:
                    newKeyList = keyList[:]
                    newKeyList.remove(key)

                    newCloseChestList = closeChestList[:]
                    newCloseChestList.remove(ch)

                    # Adding new keys
                    newKeyList.extend(ch.keys)
                    
                    # Check this is viable
                    isViable = 1
                    
                    for subch in newCloseChestList:
                        if subch.keyToOpen not in newKeyList:

                            # Maybe in the key we can get
                            isThereAnHope = 0
                            
                            for subsubch in newCloseChestList:
                                if subsubch != subch:
                                    if subch.keyToOpen in subsubch.keys:
                                        isThereAnHope = 1
                                        break
                        
                            if isThereAnHope == 0:
                                isViable = 0
#                                print "is not viable", newcurrent, subch.index, subch.keyToOpen, newKeyList, keyList[:]
                            
#                                map(showChest, newCloseChestList)
#                                for subsubch in newCloseChestList:
#                                    print "->", subsubch.keys

                                break

                    if len(string) > 0:
                        newstring = string + " " + str(ch.index)
                    else:
                        newstring = str(ch.index)
            
                    if isViable and openChest(newKeyList, chestList, newCloseChestList, newstring, newcurrent):
                        return 1
#                    else:
#                        badstart.append(newcurrent)

#                else:
#                    print "early abort for", newcurrent
#                    print

    # No key!
#    print "Fail for ", current
#    badstart.append(current)
    return 0

class myChest:
    def __init__(self, index, isOpen, keyToOpen, nbKeys, keys):
        self.index = index
        self.keyToOpen = keyToOpen
        self.isOpen = isOpen
        self.nbKeys = nbKeys
        self.keys = keys

def showChest(c):
        print "your chest: ", c.index, c.keyToOpen, c.isOpen, c.nbKeys, c.keys

for sample in range(nbSamples):

    print "Case #" + str(currSample) + ":",
    currSample = currSample + 1

    k, n = map(int, data.pop(0).rstrip().split())

#    print "k n", k, n

    startKey = map(int, data.pop(0).strip().split())

#    print "start keys:", startKey

    chestList = []
    badstart = []

    for i in range(n):
        newchest = map(int, data.pop(0).strip().split())
        c = myChest(i+1, 0, newchest[0], newchest[1], newchest[2:])
        
        chestList.append(c)
#        showChest(c)

    # Check that this would be doable, somehow
    nbKeys = {}

    for i in range(300):
        nbKeys[i] = 0

    for k in startKey:
        nbKeys[k] = nbKeys[k] + 1

    for ch in chestList:
        for k in ch.keys:
            nbKeys[k] = nbKeys[k] + 1

#    print nbKeys

    nbNeededKeys = {}

    for i in range(300):
        nbNeededKeys[i] = 0

    for ch in chestList:
        k = ch.keyToOpen
        nbNeededKeys[k] = nbNeededKeys[k] + 1

#    print nbNeededKeys
#
#    for i in range(300):
#        if nbKeys[i] != 0:
#            print "You have possibly ", nbKeys[i], "keys of type ", i
#
#    for i in range(300):
#        if nbNeededKeys[i] != 0:
#            print "You need ", nbNeededKeys[i], "keys of type ", i
#

    isImp = 0

    for i in range(300):
        if nbKeys[i] < nbNeededKeys[i]:
#            print "There will be a problem for key", i
            print "IMPOSSIBLE"
            isImp = 1
            continue

    if isImp:
        continue

    if not openChest(startKey, chestList, chestList, "", []):
        print "IMPOSSIBLE"

