#!/usr/bin/env python3

NUM_ROWS = 4
NUM_COLUMNS = 4


def run(instream):

    num_tests = int(instream.readline())

    for num_test in range(1, num_tests+1):
        validate_game(instream, num_test)


def validate_game(instream, num_test):

    row1, cards1 = read_row_and_cards(instream)
    row2, cards2 = read_row_and_cards(instream)

    validate_answers(num_test, row1, cards1, row2, cards2)


def read_row_and_cards(instream):

    row = int(instream.readline())
    cards = []
    for _ in range(1, NUM_ROWS+1):
        line = instream.readline()
        cards += [int(card_str) for card_str in line.split(" ")]

    return row, cards


def validate_answers(num_test, row1, cards1, row2, cards2):

    first_cards = get_cards_in_row(cards1, row1)
    seconds_cards = get_cards_in_row(cards2, row2)
    intersection_cards = set(first_cards).intersection(set(seconds_cards))

    num_intersection = len(intersection_cards)

    if num_intersection == 1:
        print(str.format("Case #{}: {}", num_test, list(intersection_cards)[0]))
    elif num_intersection == 0:
        print(str.format("Case #{}: Volunteer cheated!", num_test))
    else:
        print(str.format("Case #{}: Bad magician!", num_test))


def get_cards_in_row(cards, row):

    offset = NUM_COLUMNS * (row - 1)

    return cards[offset:offset+NUM_COLUMNS]

# ========== MAIN ==========

if __name__ == "__main__":

    import sys

    run(sys.stdin)


