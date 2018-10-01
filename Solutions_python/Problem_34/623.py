import sys

def create_input(input_line):
    result = []
    int_result = []
    multiple = 0

    for i in input_line:
        if (not multiple):
            if (i == '('):
                multiple = 1
            else:
                int_result.append(i)
                result.append(int_result)
                int_result = []
        else:
            if (i == ')'):
                multiple = 0
                result.append(int_result)
                int_result = []
            else:
                int_result.append(i)

    return result

def scan_wordlist(inputlist, wordlist):
    total = 0
    for i in wordlist:
        found = 1
        for j,k in zip(i,inputlist):
            if not (j in k):
                found = 0
                break
        if (found):
            total = total + 1
    return total

            

if __name__ == '__main__':

    fdin = open('A-large.in')
    fdout = open('A-large.out', 'w')

    line = fdin.readline()
    params = line.split()
    words = int(params[1])
    inputlines = int(params[2])
    wordlist = []

    for i in range(1, words + 1):
        wordlist.append(fdin.readline()[:-1])

    for i in range(1, inputlines +1):
        line = fdin.readline()[:-1]
        ans = scan_wordlist(create_input(line), wordlist)
        fdout.write('Case #%s: %s\n' % (i, ans))

    fdin.close()
    fdout.close()


        
    
