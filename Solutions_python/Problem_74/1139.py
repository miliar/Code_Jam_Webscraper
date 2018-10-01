data = open('data(2).in', 'r')

testNum = int(data.readline())

for x in range(testNum):
    input = data.readline().split()
    heldTurns = 0
    orange = 1
    blue = 1
    last = False #false = orange || true = blue
    totalSteps = 0
    turns = int(input[0])
    input = input[1:]
    for point in range(turns):
        bot = input[point*2]
        button = int(input[(point*2)+1])
        if point == 0:
            stepsTaken = 0
            if bot == 'O':
                stepsTaken = abs(button-orange)
                orange = button
                last = False
            elif bot == 'B':
                stepsTaken = abs(button-blue)
                blue = button
                last = True
            heldTurns = stepsTaken + 1 
            totalSteps += heldTurns
        else:
            stepsTaken = 0
            curr = False
            if bot == 'O':
                stepsTaken = abs(button-orange)
                orange = button
                curr = False
            elif bot == 'B':
                stepsTaken = abs(button-blue)
                blue = button
                curr = True
            if bool(curr) ^ bool(last):
                if stepsTaken != 0:
                    if heldTurns < stepsTaken:
                        stepsTaken -= heldTurns
                    else:
                        stepsTaken = 0
                heldTurns = 0
            heldTurns += stepsTaken  +1
            totalSteps += stepsTaken  +1
            last = curr
    print('Case #' + str(x+1) + ': ' + str(totalSteps))
        
        
    