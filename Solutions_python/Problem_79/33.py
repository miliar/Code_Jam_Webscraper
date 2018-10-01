#!/usr/bin/env python

import fileinput, collections, sys, operator, itertools

def autodict():
    return collections.defaultdict(autodict)

def input():
    it = iter(itertools.imap(str.rstrip, fileinput.input()))
    it.next()
    while True:
        n,m = map(int,it.next().split())
        words = []
        for i in range(n):
            words.append(it.next())
        lists = []
        for i in range(m):
            lists.append(it.next())
        yield (words,lists)

def group(words):
    res = {}
    for word in words:
        x = len(word)
        if not x in res:
            res[x] = []
        res[x].append(word)
    return res

def nextguess(words, list):
    letters = set()
    for word in words:
        for let in word:
            letters.add(let)
    for i,let in enumerate(list):
        if let in letters:
            return (i,let)
    raise "Oops"
    return (None, None)

def genlettermap(letters):
    map = {}
    for i,l in enumerate(letters):
        map[l] = i
    return map

def diffpoint(word1,word2,lettermap):
    res = 10000
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            res = min(res,lettermap[word1[i]],lettermap[word2[i]])
    if res == 10000:
        print 'FAIL %s %s' % (word1,word2)
        sys.exit()
    return res

def value(word, dps, letters):
    ret = 0
    for dp in dps:
        if letters[dp] not in word:
            ret += 1
    return ret

def compatible(w1,w2,letterschosen):
    if len(w1) != len(w2): return False
    for i in range(len(w1)):
        if w1[i] != w2[i] and (w1[i] in letterschosen or w2[i] in letterschosen):
            return False
    return True

def filterwords(w1,words,letterschosen):
    newwords = []
    for word in words:
        if compatible(w1,word,letterschosen):
            newwords.append(word)
    return newwords

def scoreword(word, allwords, letters):
    letterschosen = set()
    points = 0
    allwords = filterwords(word,allwords,letterschosen)
    while len(allwords) > 1:
        i,nextletter = nextguess(allwords, letters)
        letters = letters[i+1:]
        letterschosen.add(nextletter)
        if nextletter not in word:
            points += 1
        allwords = filterwords(word,allwords,letterschosen)
    return points

def main():
    for casenum, (words,lists) in enumerate(input()):
        wgroups = group(words)
        res = []
        for list in lists:
            bestword = ''
            bestvalue = -1
            #print list
            lmap = genlettermap(list)
            for w1 in words:
                dps = set()
                for w2 in words:
                    if len(w1) != len(w2) or w1 == w2: continue
                    p = diffpoint(w1,w2,lmap)
                    dps.add(p)
                v = value(w1, dps, list)
                if v > bestvalue:
                    bestvalue = v
                    bestword = w1
                #vv = scoreword(w1,words,list)
                #if v != vv: print 'moop'
                #print w1,dps,v,vv
            res.append(bestword)
        #print group(words); continue
        # code
        print "Case #%d: %s" % (casenum+1, ' '.join(res))

main()
