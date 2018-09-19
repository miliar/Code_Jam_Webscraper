#Open input
case_file = open('Sample.txt')
total_cases = int(case_file.readline())
case_string = case_file.read()
lines= case_string.splitlines()
output = open("output.txt")



for case in xrange(1, total_cases +1):
    first = int(lines[(case-1) *10])
    rowfirst = [lines[(case-1) *10 +1], lines[(case-1) *10 +2 ], lines[(case-1) *10 +3], lines[(case-1) *10+ 4]]
    second = int(lines[(case-1) *10 +5])
    rowsecond = rows = [lines[(case-1) *10 +6], lines[(case-1) *10 +7 ], lines[(case-1) *10 +8], lines[(case-1) *10+ 9]]
    options = 0

    cards1 = rowfirst[first-1].split()
    cards2 = rowsecond[second-1].split()
    for card in cards1:
        if card in cards2:
            options += 1
            cardnumber = card
    if options == 0:
        print "Case #{0}: Volunteer cheated!".format(case)
    if options > 1:
        print "Case #{0}: Bad magician!".format(case)
    if options == 1:
        print "Case #{0}: {1}".format(case, cardnumber)