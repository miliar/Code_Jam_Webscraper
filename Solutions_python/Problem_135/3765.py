datain = open('A-small-attempt0.in', 'r')
dataout = open('dataout.txt', 'w')



for length in range(int(datain.readline())):
    PickedRow = int(datain.readline())-1
    for tries in range(4):
        NextRow = map(int, datain.readline().split())
        if tries == PickedRow:
            Row1 = NextRow
    PickedRow2 = int(datain.readline())-1
    for tries in range(4):
        NextRow = map(int, datain.readline().split())
        if tries == PickedRow2:
            Row2 = NextRow
    answer = 0
    answer2 = 0
    for cards in Row1:
            if cards in Row2:
                answer+=1
                answer2 = cards
    
    if answer == 1:
        print("Case #" + str(length+1) + ": " + str(answer2))
    if answer == 0:
        print("Case #" + str(length+1) + ": Volunteer cheated!")
    if answer > 1:
        print("Case #" + str(length+1) + ": Bad Magician!")