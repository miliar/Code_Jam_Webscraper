#!/usr/bin/env python3.3
"""
Google Code Jam 2013 Qualification Round
Problem A: Tic-Tac-Toe-Tomek

Determine inputted game state using given rules.

@author Jeffrey Owens
"""

"""
Determine whether the given string wins Tic-Tac-Toe-Tomek
Returns whether it is a win and the winner (blank if none)
"""
def isWinningString(input):
    if 'X' in input and 'O' in input:    # If both X and O exist, not a win
        return False, ''
    elif '.' in input:   # If input is not filled with letters, not a win
        return False,''
    else:       # Winner!
        # Avoid declaring T the winner
        if input[0] == 'T':
            winner = input[1]
        else:
            winner = input[0]

        return True, winner

inputFile = 'A-large.in'
outputFile = 'A-large.out'

input = open(inputFile, 'r')
# Read the number of cases
numCases = int(input.readline())

output = open(outputFile, 'w')

for case in range(1, numCases + 1):
    
    #(Re)declare empty list
    board = list()
    
    # Read the board into the list
    for i in range(0, 4):
                                # Strip newlines
        board.append(list(input.readline().rstrip()))

    # Skip over blank line
    input.readline()

    # Predeclare, just in case
    win = False
    draw = False
    winner = ''

    # Check if there is a winner in the rows
    for row in board:
                                                    # list to string
        win, winner = isWinningString(''.join(row))
        if win is True: # stop search if win found
            break
    
    # end for (row)

    # Diagnal check for winner
    if win is False:
        # Continue search for winner
        
        # Search diagnals (only 2, yay!)
        for i in range(0, 2):
            stringInput = ''
            if i is 0:  # Check first diagonal
                for j, row in enumerate(board):
                    stringInput = stringInput + row[j]

            else:
                for j, row in enumerate(board):
                    stringInput = stringInput + row[-(j+1)]

            win, winner = isWinningString(stringInput)
            if win is True: # stop search if win found
                break
            
    # end if (diagnals)

    # Column check for winner (more expensive)
    if win is False:
        # Continue searching for a winner
        
        # Search columns for winner
        # Have to manually loop 4 times (sad)
        for i in range(0, 4):
            stringInput = ''
            # Build column string
            for row in board:
                stringInput = stringInput + row[i]

            win, winner = isWinningString(stringInput)
            if win is True: # stop search if win found
                break

    # end if (columns)

    # Draw test
    if win is False:
        # SInce there is no winner, determine if game is a draw

        # Presume game is a draw
        draw = True

        # Search for move that would make game not a draw
        for row in board:

            if '.' in row: # Stop search if valid move can still be made
                draw = False
                break
    # end if (draw)

    # Output result, to console and to file
    stringOut = 'Case #' + str(case) + ': '
    if win is True:
        # Print winner
        stringOut = stringOut + winner + ' won'
        print(stringOut)
        output.write(stringOut + '\n')
    else:    # If win is false
        if draw is True:
            stringOut = stringOut + 'Draw'
            print(stringOut)
            output.write(stringOut + '\n')
        else:
            stringOut = stringOut + 'Game has not completed'
            print(stringOut)
            output.write(stringOut + '\n')

# end for (case)

# Cleanup
input.close()
output.close()
