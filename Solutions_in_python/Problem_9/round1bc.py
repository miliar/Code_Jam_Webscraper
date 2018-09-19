from helper_functions import *
from scipy import zeros, int32

def solve_problem(input, output):
    n_cases = getnum(input)
    for case in range(n_cases):
        n_cards = getnum(input)
        ds = getnums(input)[1:]
        ds = [d-1 for d in ds]
        cards = create_perfect(n_cards)
        print cards
        answers = [str(k) for k in cards[ds]]
        answer(' '.join(answers), output)
        
def create_perfect(n_cards):
    cards = zeros(n_cards, dtype=int32)
    empty_spaces = range(n_cards)
    deck_rotation = 0
    for i in xrange(n_cards):
        l = n_cards - i # = len(empty_spaces)
        deck_rotation = (i+deck_rotation) % l
        index = empty_spaces[deck_rotation]
        cards[index] = i+1
        empty_spaces.pop(deck_rotation)
    return cards
    

if __name__ == "__main__":
    test_input = """2
5
5 1 2 3 4 5
15
4 3 4 7 10"""
    test_output = """Case #1: 1 3 2 5 4
Case #2: 2 8 13 4"""
    
    do_test(solve_problem, test_input, test_output)
    
    do_real(solve_problem)