#!/usr/bin/python
import os, sys, collections

def simplify(combiners, opposers, l, count):
    # first run combiners
    #print count
    newToCheck = []
    if len(l) > 0:
        newToCheck.append(l[-1])
    while len(l) > 1:
        pair = (l[len(l)-1], l[len(l)-2])
        if pair in combiners:
            #print 'COMBINING'
            new = combiners[pair]
            count[pair[0]] -= 1
            count[pair[1]] -= 1
            count[new] += 1
            newToCheck.append(new)
            l.pop()
            l.pop()
            l.append(new)
            #print 'C: %s' % l
            #l = l[:-2] + [new]
        else:
            break
    # now run opposers
    #print newToCheck
    if len(l) > 1:
        for n in newToCheck:
            if n in opposers and count[n] > 0:
                for other in opposers[n]:
                    if count[other] > 0:
                        # boom!
                        #print count
                        return True
    return False

def runMagic(combiners, opposers, s):
    l = []
    count = collections.defaultdict(int)
    for c in s:
        c = ord(c)
        l.append(c)
        count[c] += 1
        if simplify(combiners, opposers, l, count):
            # boom!
            count = collections.defaultdict(int)
            l = []
        #print l
    return l

def main(filename):
    fileLines = open(filename, 'r').readlines()
    index = 0
    numCases = int(fileLines[index][:-1])
    index += 1
    for caseNum in range(numCases):
        caseStr = fileLines[index][:-1]
        index += 1
        nums = [x for x in caseStr.split(' ')]
        i = 0
        numCombiners = int(nums[i])
        i += 1
        combinersStrs = nums[i:i+numCombiners]
        i += numCombiners
        numOpposers = int(nums[i])
        i += 1
        opposersStrs = nums[i:i+numOpposers]
        i += numOpposers
        # don't care about num of chars
        i += 1
        actualStr = nums[i] 
        i += 1
        if (i != len(nums)):
            print 'Uh-oh, case %d has wrong len (i is %d, len is %d)' % (caseNum, i, len(nums))
        combiners = {}
        for s in combinersStrs:
            combiners[(ord(s[0]), ord(s[1]))] = ord(s[2])
            combiners[(ord(s[1]), ord(s[0]))] = ord(s[2])
        #print combiners
        opposers = {}
        for s in opposersStrs:
            if ord(s[0]) not in opposers:
                opposers[ord(s[0])] = set()
            opposers[ord(s[0])].add(ord(s[1]))
            if ord(s[1]) not in opposers:
                opposers[ord(s[1])] = set()
            opposers[ord(s[1])].add(ord(s[0]))
        #print opposers
        l = runMagic(combiners, opposers, actualStr)
        l = [chr(x) for x in l]
        s = '[' + ', '.join(l) + ']'
        #print caseStr
        print "Case #%d: %s" % (caseNum + 1, s)

if __name__ == '__main__':
    main(sys.argv[1])
