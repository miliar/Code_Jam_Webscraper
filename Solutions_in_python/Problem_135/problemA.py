SIZE = 10
with open('A-small-attempt3.in') as f:
    contents = f.readlines()
count = int(contents[0])
for i in range(1, count*SIZE, SIZE):
    itter = i/SIZE+1
    answer1 = int(contents[i])
    card_row1 = set(contents[i+answer1].split())
    answer2 = int(contents[i+5])
    card_row2 = set(contents[i+5+answer2].split())
    inter = card_row1 & card_row2
    if len(inter) == 1:
        print "Case #{0}: {1}".format(itter, list(inter)[0])
    if len(inter) > 1:
        print "Case #{0}: Bad magician!".format(itter)
    if len(inter) == 0:
        print "Case #{0}: Volunteer cheated!".format(itter)
