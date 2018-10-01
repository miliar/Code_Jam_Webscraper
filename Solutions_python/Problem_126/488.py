import itertools

def readFile(filename):
    f = open(filename, 'r')
    totalCases = int(f.readline()[:-1])
    cases = []
    for _ in range(totalCases):
        line = f.readline()
        if '\n' in line:
            line = line[:-1]
        case = line.split(' ')
        cases.append(case)
    f.close()
    return cases

output = lambda results: '\n'.join(['Case #' + str(index + 1) + ": " + str(result) for index, result in enumerate(results)])

def main(infile, outfile):
    cases = readFile(infile)
    results = computeResults(cases)
    f = open(outfile, 'w')
    f.write(output(results))
    f.close()

def substrings(s, min_length=1):
    results = []
    for length in range(min_length, len(s)+1):
        for start in range(len(s) - min_length + 1):
            substring = s[start:start+length]
            if len(substring) == length:
                results.append(substring)
    return results

def isConsonant(letter):
    return letter in 'bcdfghjklmnpqrstvwxyz'

def computeResults(cases):
    results = []
    for case in cases:
        name = case[0]
        n = int(case[1])
        substringCounter = 0
        sStrings = substrings(name, n)
        for substring in sStrings:
            counter = 0
            for letter in substring:
                counter = counter + 1 if isConsonant(letter) else 0
                if counter >= n:
                    substringCounter += 1
                    break
        results.append(substringCounter)
    return results

infile = 'A-small-attempt0.in'
outfile = 'A-small.out'
main(infile, outfile)