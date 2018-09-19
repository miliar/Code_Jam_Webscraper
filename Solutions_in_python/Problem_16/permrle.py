import sys

f = open(sys.argv[1])

o = open(sys.argv[1].split('.')[0] + '.out', 'w')

nCases = int(f.readline().strip())

def permute (word):
    retList=[]
    if len(word) == 1:
        # There is only one possible permutation
        retList.append(word)
    else:
        # Return a list of all permutations using all characters
        for pos in range(len(word)):
            # Get the permutations of the rest of the word 
            permuteList=permute(word[0:pos]+word[pos+1:len(word)])
            # Now, tack the first char onto each word in the list
            # and add it to the output
            for item in permuteList:
                retList.append([word[pos]]+item)
    return retList


def compress(p, s):
    result = []
    for i in range(len(s) / len(p)):
        t = ['a' for k in range(len(p))]
        for j in range(len(p)):
            t[j] = s[len(p)*i + p[j]]
        result.append(''.join(t))
    return ''.join(result)
            
def size(s):
    current = s[0]
    count = 1
    for c in s[1:]:
        if c != current:
            current = c
            count += 1
    return count

for case in range(nCases):
    k = int(f.readline().strip())
    s = f.readline().strip()

    permutes = permute(range(k))

    min_size = float('infinity')

    for p in permutes:
        compressed = compress(p, s)
        min_size = min(min_size, size(compressed))

    #print min_size                     

                  

    o.write('Case #%d: %d\n' % (case + 1, min_size))
