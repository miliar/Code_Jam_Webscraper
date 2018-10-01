import sys
from collections import deque

out_file = open('output.out','w+')
in_file = sys.stdin
num_cases = int(in_file.readline().strip('\n'))
num_cases += 1

for c in range(1, num_cases):
    blue = deque()
    orange = deque()

    case = 'Case #' + str(c) + ': '
    case_info = in_file.readline().strip('\n').split(' ')

    buttons = int(case_info[0])

    counter = 1
    x = 0
    while (counter < len(case_info)):
        if (case_info[counter] == 'B'):
            blue.append((x, int(case_info[counter + 1])))
        else:
            orange.append((x, int(case_info[counter + 1])))

        counter += 2
        x += 1

    turn = 0
    blue_label = 1
    orange_label = 1
    steps = 0

    while True:
        #Ninguna de las dos listas esta vacia
        if (blue and orange):
            #Turno del robot azul
            if (blue[0][0] == turn):
                #print 'B\'s turn: ' + str(turn)
                #Azul moverse hacia adelante
                if (blue[0][1] > blue_label):
                    blue_label += 1
                    steps += 1
                    #print 'B: Move to button ' + str(blue_label)
                #Presionar el botton azul
                elif (blue[0][1] == blue_label):
                    steps += 1
                    blue.popleft()
                    turn += 1
                    #print 'B: Push button ' + str(blue_label)
                #Azul moverse hacia atras
                else:
                    blue_label -= 1
                    steps += 1
                    #print 'B: Move to button ' + str(blue_label)

                #Anaranjado moverse hacia adelante
                if (orange[0][1] > orange_label):
                    orange_label += 1
                    #print 'O: Move to button ' + str(orange_label)
                #Anaranjado moverse hacia atras
                elif (orange[0][1] < orange_label):
                    orange_label -= 1
                    #print 'O: Move to button ' + str(orange_label)
                    #print 'O: Stay at button ' + str(orange_label)
                
            #Turno del robot anaranjado
            else:
                #print 'O\'s turn: ' + str(turn)
                #Anaranjado moverse hacia adelante
                if (orange[0][1] > orange_label):
                    orange_label += 1
                    steps += 1
                    #print 'O: Move to button ' + str(orange_label)
                #Presionar el botton anaranjado
                elif (orange[0][1] == orange_label):
                    steps += 1
                    orange.popleft()
                    turn += 1
                    #print 'O: Push button ' + str(orange_label)
                #Anaranjado moverse hacia atras
                else:
                    orange_label -= 1
                    steps += 1
                    #print 'O: Move to button ' + str(orange_label)

                #Azul moverse hacia adelante
                if (blue[0][1] > blue_label):
                    blue_label += 1
                    #print 'B: Move to button ' + str(blue_label)
                #Azul moverse hacia atras
                elif (blue[0][1] < blue_label):
                    blue_label -= 1
                    #print 'B: Move to button ' + str(blue_label)
                    #print 'B: Stay at button ' + str(blue_label)
        else:
            #La lista azul esta vacia
            if (len(blue) == 0 and len(orange) != 0):
                #print 'O\'s turn: ' + str(turn)
                #Anaranjado moverse hacia adelante
                if (orange[0][1] > orange_label):
                    orange_label += 1
                    steps += 1
                    #print 'O: Move to button ' + str(orange_label)
                #Presionar el botton anaranjado
                elif (orange[0][1] == orange_label):
                    steps += 1
                    orange.popleft()
                    turn += 1
                    #print 'O: Push button ' + str(orange_label)
                #Anaranjado moverse hacia atras
                else:
                    orange_label -= 1
                    steps += 1
                    #print 'O: Move to button ' + str(orange_label)
            #La lista anaranjada esta vacia
            elif (len(blue) != 0 and len(orange) == 0):
                #print 'B\'s turn: ' + str(turn)
                #Azul moverse hacia adelante
                if (blue[0][1] > blue_label):
                    blue_label += 1
                    steps += 1
                    #print 'B: Move to button ' + str(blue_label)
                #Presionar el botton azul
                elif (blue[0][1] == blue_label):
                    steps += 1
                    blue.popleft()
                    turn += 1
                    #print 'B: Push button ' + str(blue_label)
                #Azul moverse hacia atras
                else:
                    blue_label -= 1
                    steps += 1
                    #print 'B: Move to button ' + str(blue_label)
            else:
                break

    out_file.write(case + str(steps) + '\n')
