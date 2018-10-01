# Read input
lines = [line.strip() for line in open('A-large.in', 'r')]

# Select output file
open('A-large.out', 'w').write('')
def print_to_file(line):

    open('A-large.out', 'a').write(line + '\n')
    

# First element is just the number of games
lines.pop(0)


# Parse each game
games = [[]]
game_count = 0
game_line_width = 4
game_line_count = 4

for line in lines:
    
    if len(line) == game_line_width:

        # Add new game
        if len(games[game_count]) >= game_line_count:
            games.append([])
            game_count += 1
        
        # Add line to game
        if len(games[game_count]) < game_line_count:
            games[game_count].append(line)

# Evaluate each game

def whowon(lines):
  
    for line in lines:

        line = line.replace('T', '')
        
        if line == 'XXX' or line == 'XXXX':

                return 'X won'

        elif line == 'OOO' or line == 'OOOO':

                return 'O won'

    else:

        return False

game_count = 0

for game in games:

    game_count += 1

    # Check horizontally
    result = whowon(game)
    if result != False:
        print_to_file('Case #' + str(game_count) + ': ' + result)
        continue

    #  Check vertically
    columns = ['', '', '', '']
    
    for line in game:

        for i in range(len(line)):
            
            columns[i] = columns[i] + line[i]

    result = whowon(columns)
    if result !=  False:
        print_to_file('Case #' + str(game_count) + ': ' + result)
        continue

    # Check diagonally
    diag1 = game[0][0] + game[1][1] + game[2][2] + game[3][3]
    diag2 = game[0][3] + game[1][2] + game[2][1] + game[3][0]

    result = whowon([diag1, diag2])
    if result !=  False:
        print_to_file('Case #' + str(game_count) + ': ' + result)
        continue

    # Check not-completed & draw
    for line in game:
        if line.find('.') != -1:
            print_to_file('Case #' + str(game_count) + ': Game has not completed')
            break
    else:
        print_to_file('Case #' + str(game_count) + ': Draw')
        
    
