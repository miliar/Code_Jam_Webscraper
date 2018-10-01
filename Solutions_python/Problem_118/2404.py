import sys

filename = sys.argv[1]
curfile = file(filename, 'rb')

outputfile = file("fairoutput1.txt", 'wb')

largestvalue = 0
lines = curfile.readlines()

if lines[0].strip().isdigit():
    numcases = int(lines[0])

ranges = []
for line in lines[1:]:
    start = int(line.split(' ')[0])
    end = int(line.split(' ')[1])
    if end > largestvalue:
        largestvalue = end
    ranges.append((start, end))

print ranges

numbers = []

count = 1
while count <= largestvalue:
    countstring = str(count)
    curnum = pow(count, 2)
    numstring = str(curnum)
##    if count > 100000:
##        if (numstring[0] != '1') & (numstring[0] != '4') & (numstring[0] != '9'):
##            count+1
##            continue
    if countstring[0] == countstring[len(countstring)-1]:
        if countstring == countstring[::-1]:
            if numstring == numstring[::-1]:
                numbers.append(curnum)
                print curnum
    count += 1

count = 0
for range in ranges:
    value = 0
    for number in numbers:
        if (number >= range[0]) & (number <= range[1]):
            value += 1
        elif number > range[1]:
            break
    outputfile.write("Case #%i: %i\r\n" % (count + 1, value))
    count += 1

outputfile.close()
