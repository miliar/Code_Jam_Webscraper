def isTidy(number):
    number = str(number)

    if len(number) == 1:
        return True

    for i in range(len(number)-1):
        first = number[i]
        second = number[i+1]
        if second < first:
            return False

    return True
def makeTidy(number):
    number = list(str(number))
    for i in range(len(number)-1):
        first = number[i]
        second = number[i+1]
        if second < first:
            #first minus 1, make all 9 from second digit onwards
            number[i] = str(int(first)-1)
            for j in range(i+1,len(number)):
                number[j] = '9'
            break
    return ''.join(number)

def findTidy(number):

    while not isTidy(number):
        number = int(makeTidy(number))

    return int(number)


infilename = "B-large.in"
infile = open(infilename, 'r')
lines = infile.readlines()

cases = []
t = int(lines[0].strip('\n'))
for i in range(1,t+1):
    cases.append(lines[i].strip('\n'))

infile.close()

outfile = open("B-large.out", 'w')

caseNo = 1
for case in cases:
    result = findTidy(case)
    outfile.write("Case #{}: {}\n".format(caseNo, result))
    caseNo += 1

outfile.close()
