f = open('input.txt', 'r')
case_count = f.readline()
for case in range(int(case_count)):
    res = []
    matrice_A = {}
    matrice_B = {}
    choice_A = int(f.readline()[:-1]) -1
    for i in range(4):
        matrice_A[i] = f.readline()[:-1]
    choice_B = int(f.readline()[:-1]) - 1
    for i in range(4):
        matrice_B[i] = f.readline()[:-1]
    for card in matrice_A[choice_A].split(' '):
        if card in matrice_B[choice_B].split(' '):
            res.append(card)
    # Result print
    if len(res) == 1: 
        print "Case #%s: %s" %(str(int(case) + 1), res[0])
    elif len(res) > 1:
        print "Case #%s: Bad magician!" % str(int(case) + 1)
    else:
        print "Case #%s: Volunteer cheated!" % str(int(case) + 1)

    



