from collections import defaultdict
import sys

def _solve_line(line):
    sol = []
    empty_chars_prefix = 0
    for c in line:
        if c != '?':
            # New child
            sol.append(c)
        elif sol:
            # Repeat last child
            sol.append(sol[-1])
        else:
            # Repeat first child, but we don't know who it is yet.
            empty_chars_prefix += 1

    if empty_chars_prefix > 0:
        sol = ([sol[0]] * empty_chars_prefix) + sol
    return ''.join(sol)

def assign_children(board):
    sol = []
    empty_lines_top = 0
    for line in board:
        if not all(c=='?' for c in line):
            # New line style
            sol.append(_solve_line(line))
        elif sol:
            # Repeat last line
            sol.append(sol[-1])
        else:
            # Repeat first line, but we don't know what it is yet.
            empty_lines_top += 1

    if empty_lines_top > 0:
        sol = ([sol[0]] * empty_lines_top) + sol
    return sol

if __name__ == "__main__":
    ncases = int(sys.stdin.readline().strip())
    for i in range(ncases):
        R, C = [int(part) for part in sys.stdin.readline().split()]
        board = []
        for _ in range(R):
            line = sys.stdin.readline().strip()
            assert len(line) == C
            assert all(c=='?' or 'A'<=c<='Z' for c in line)
            board.append(line)
        sol = assign_children(board)
        print "Case #%d:" % (i+1)
        for sol_line in sol:
            print sol_line
