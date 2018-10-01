import sys


def do_trick(cue1, cue2, grid1, grid2):
    cue1_row = grid1[cue1-1]
    cue2_row = grid2[cue2-1]

    # That's the meat of it. One line...
    magic_guesses = [card for card in cue1_row if card in cue2_row]

    if len(magic_guesses) == 0:
        return "Volunteer cheated!"
    elif len(magic_guesses) == 1:
        return magic_guesses[0]
    else:
        return "Bad magician!"


if __name__ == "__main__":
    lines = open(sys.argv[1]).readlines()
    num_test_case = int(lines[0].strip())
    test_case_lines = lines[1:]

    num_test_case_executed =  0
    while num_test_case_executed != num_test_case:
        test_case_start_line = num_test_case_executed * 10;
        test_case_end_line = num_test_case_executed * 10 + 10;
        relevant_lines = test_case_lines[test_case_start_line:test_case_end_line]

        result = do_trick(
            int(relevant_lines[0].strip()),
            int(relevant_lines[5].strip()),
            [line.split() for line in relevant_lines[1:5]],
            [line.split() for line in relevant_lines[6:10]],
        )

        num_test_case_executed += 1
        print "Case #%s: %s" % (num_test_case_executed, result)

else:
    print "Don't import. Please invoke with `python <this_file.py> <your_input>`"
