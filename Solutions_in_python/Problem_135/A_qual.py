cas = int(raw_input().strip())

for c in range(1,cas+1):
    call1 = int(raw_input().strip())
    card1 = []
    for i in range(4):
        card1.append(raw_input().strip().split())
    card1 = card1[call1-1]
    
    call2 = int(raw_input().strip())
    card2 = []
    for i in range(4):
        card2.append(raw_input().strip().split())
    card2 = card2[call2-1]

    dup = []
    for i in card1:
        if i in card2:
            dup.append(i)

    if(len(dup) == 0):
        ans = 'Volunteer cheated!'
    elif(len(dup) > 1):
        ans = 'Bad magician!'
    else:
        ans = dup[0]
    
    print 'Case #' + str(c) + ': ' + ans
