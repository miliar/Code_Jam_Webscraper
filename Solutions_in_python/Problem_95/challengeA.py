# finds objects that are in listA, but not in listB
def findObjectsNotInList(listA, listB):
    returnVal = []
    for item in listA:
        if item not in listB:
            returnVal.append(item)
    return returnVal

def generateMappingForPhrases(googleresePhrases, englishPhrases):
    #given values
    returnMapping = {'y' : 'a', 'e' : 'o', 'q' : 'z'}
    # values can be joined - doesn't make a difference
    googleresePhrases = ' '.join(googleresePhrases)
    englishPhrases = ' '.join(englishPhrases)

    charIndex = 0
    for char in googleresePhrases:
        returnMapping[googleresePhrases[charIndex]] = englishPhrases[charIndex]
        charIndex += 1
    
    return returnMapping

def translateToEnglishUsingMapping(string, mapping):
    returnString = ''

    for char in string:
        returnString = returnString + mapping[char]

    return returnString
    
def challengeA():
    output = ''

    # Given values
    letterMapping = {'y' : 'a', 'e' : 'o', 'q' : 'z'}
    allLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    knownLetters = letterMapping.keys()
    googleresePhrases = ['ejp mysljylc kd kxveddknmc re jsicpdrysi', 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'de kr kd eoya kw aej tysr re ujdr lkgc jv'];
    englishPhrases = ['our language is impossible to understand', 'there are twenty six factorial possibilities', 'so it is okay if you want to just give up'];
    letterMapping = generateMappingForPhrases(googleresePhrases, englishPhrases)
    allLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    knownGooglereseLetters = letterMapping.keys()

    unknownGooglerese = findObjectsNotInList(allLetters, knownGooglereseLetters)

    knownEnglishLetters = letterMapping.values()

    unknownEnglish = findObjectsNotInList(allLetters, knownEnglishLetters)

    #assume there is only one unknown letter
    letterMapping[unknownGooglerese[0]] = unknownEnglish[0]
    
    fileString = open('/Users/Lenny/Desktop/CodeJam-2012/A-small.in', 'r').read()
    fileArray = fileString.split('\n')
    fileArray.pop(0)
    fileArray.pop(len(fileArray) - 1)

    sentenceIndex = int(1)
    
    for sentence in fileArray:
        output = output + "Case #" + str(sentenceIndex) + ": " + translateToEnglishUsingMapping(sentence, letterMapping) + "\n"
        sentenceIndex += 1

    outputFile = open('/Users/Lenny/Desktop/CodeJam-2012/A-small.out', 'w')
    outputFile.write(output)

challengeA()
