if __name__ == "__main__":
    outputseed = "the quick brown fox jumps over the lazy brown dog"
    inputseed  = "rbc zjkfo npets weh ujxvd egcp rbc myqa npets iel"

    replacedict = {}
    srcdict = {}

    i = 0
    for letter in inputseed:
        replacedict[letter] = outputseed[i]
        srcdict[outputseed[i]] = letter
        i+=1
    sentences = int(raw_input())

    j = 0

    inputsent = raw_input().split('\n')

    for sentence in inputsent:
        outsent = ""
        for letter in sentence:
            outsent += replacedict[letter]
        print "Case #" + str(j+1) + ": " + outsent
        j += 1
