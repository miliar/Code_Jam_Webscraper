#!/usr/bin/python

def lines(N):
    """ Yield each line in an N by N Tic-Tac-Toe board """
    yield slice(0, None, N + 1) # Main Diagonal 1
    yield slice(N - 1, N*N - 1, N - 1) # Main Diagonal 2
    for i in xrange(N):
        yield slice(i, None, N) # Column i
        yield slice(i * N, (i + 1) * N) # Row i

def checkLine(line):
    """ Given a line, return who wins that line (or None) if neither does """
    players = set(line) - {"T"}
    if 1 == len(players) and players != {"."}: # If one player fills the line
        return list(players)[0] # The one element in players
    else:
        return None

def checkBoard(board, N):
    """Return the status of the board"""
    for line in lines(N):
        winner = checkLine(board[line])
        if winner is not None:
            return winner + " won"
    # If we're here, then nobody won.
    return "Game has not completed" if "." in board else "Draw"

def main(N):
    cases = int(raw_input())
    for case in xrange(1, cases + 1): # 1-indexed
        # Read the board
        board = "".join([raw_input().strip() for i in xrange(N)])
        raw_input() # Discard blank line
        print "Case #{case}: {status}".format(case = case,
                                             status = checkBoard(board, N))

if __name__ == "__main__":
    main(4) # Hardcoded board size
