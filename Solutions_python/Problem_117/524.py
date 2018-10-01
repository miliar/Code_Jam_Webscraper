#!/usr/bin/env python -B

def main():
    num_cases = int(raw_input())
    for case_number in xrange(1, num_cases + 1):
        r, c = map(int, raw_input().split())
        board = []
        for i in xrange(r):
            row = map(int, raw_input().split())
            board.append(row)

        left = [-1] * r
        top = [-1] * c
        for i in xrange(r):
            for j in xrange(c):
                left[i] = max(left[i], board[i][j])
                top[j] = max(top[j], board[i][j])

        produced_board = [[0] * c for i in xrange(r)]
        for i in xrange(r):
            for j in xrange(c):
                produced_board[i][j] = min(left[i], top[j])

        if produced_board == board:
            print "Case #{}: YES".format(case_number)
        else:
            print "Case #{}: NO".format(case_number)

if __name__ == "__main__":
    import b
    b.main()
