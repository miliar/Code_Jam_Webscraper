# google codejam qualifier
# solution for problem A
import sys
from case_io import CaseIO

WILDCARD = "T"
EMPTY = "."

OUT_FILE = "qualifier-a.out"

def same_sign(element, sign):
    return element == sign or element == "T"

def winner(vector):
    """
    determine winner of this vector
    """
    first = vector[0]
    if first == EMPTY:
        return None
    elif first == WILDCARD:
        return winner(vector[1:])
    elif all([same_sign(element, first) for element in vector[1:]]):
        return first
    else:
        return None
       
def has_not_ended(board):
    return any((element == EMPTY for vector in board for element in vector))
       
def make_vectors(board):
    """
    yield the possible win vectors from the 4x4 board given as list of rows
    """
    # rows
    for vector in board:
        yield [sign for sign in vector]
    # cols
    for vector in zip(*[line for line in board]):
        yield list(vector)
    # diagonals
    yield [board[pos][pos] for pos in range(4)]
    yield [board[pos][3-pos] for pos in range(4)]
    
def make_answer(winner_sign, case):
    if winner_sign is not None:
        return "{} won".format(winner_sign)
    elif has_not_ended(case):
        return "Game has not completed"
    else:
        return "Draw"
    
if __name__ == "__main__":
    io = CaseIO(sys.argv[1], OUT_FILE, 4, True)
    for case in io.cases():
        vectors = make_vectors(case)
        vector_results = (winner(vector) for vector in vectors)
        winner_sign = next((result for result in vector_results if result is not None), None)
        io.write(make_answer(winner_sign, case))
        