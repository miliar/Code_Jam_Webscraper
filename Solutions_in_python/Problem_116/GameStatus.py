### SYSTEM IMPORTS ###
from __future__ import with_statement
import sys
### PACKAGE IMPORTS ###
from GameBoard import GameBoard

### CONSTANTS ###
OUTPUT_FILEPATH = "output"

def main():
    if len(sys.argv) != 2:
        print("Usage: %s <input_filepath>" % (sys.argv[0]))
        exit()
    filepath = sys.argv[1]
    output_file = open(OUTPUT_FILEPATH, "w")
    '''
    lines = input_file.readlines()[1:]
    input_file.close()
    '''
    num_of_test_cases = 0
    with open(filepath, 'r') as input_file:
        it = iter(input_file)
        num_of_test_cases  = int(next(it))
        test_case_board = []
        test_case_id = 1
        for line in it:
            if line.isspace():
                if test_case_board:
                    game_board = GameBoard(test_case_board)
                    if not test_case_id == 1:
                        output_file.write('\n')
                    output_file.write("Case #%d: " % (test_case_id))
                    output_file.write("%s" % (game_board.get_game_status_message()))
                    test_case_board = []
                    test_case_id += 1
            else:
                line = line[:-1]
                test_case_board.append(line)

    output_file.close()
    return

if __name__ == "__main__":
    main()