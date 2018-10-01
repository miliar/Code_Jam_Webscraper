BISHOP = '+'
ROOK = 'x'
QUEEN = 'o'

if __name__ == "__main__":
    T = int(raw_input())
    for t in range(T):
        N, M = map(int, raw_input().strip().split(" "))
        bishops = [[False for _ in range(N)] for _ in range(N)]
        rooks = [[False for _ in range(N)] for _ in range(N)]

        cols = [False for _ in range(N)]
        rows = [False for _ in range(N)]
        diagonals_sum = set()
        diagonals_diff = set()

        score = 0
        for m in range(M):
            piece, r, c = raw_input().strip().split(" ")
            r = int(r) - 1
            assert r == 0
            c = int(c) - 1
            if piece == QUEEN:
                score += 2
            else:
                score += 1

            if piece == BISHOP or piece == QUEEN:
                bishops[r][c] = True
                diagonals_sum.add(r + c)
                diagonals_diff.add(r - c)
            if piece == ROOK or piece == QUEEN:
                rooks[r][c] = True
                rows[r] = True
                cols[c] = True

        pieces = []
        for r in [0, N - 1]:
            for c in range(N):
                if ((r + c) not in diagonals_sum) and \
                   ((r - c) not in diagonals_diff):
                    diagonals_sum.add(r + c)
                    diagonals_diff.add(r - c)
                    assert bishops[r][c] is False
                    if rooks[r][c]:
                        pieces.append((QUEEN, r, c))
                        score += 1
                    elif not rows[r] and not cols[c]:
                        pieces.append((QUEEN, r, c))
                        score += 2
                        rows[r] = True
                        cols[c] = True
                    else:
                        pieces.append((BISHOP, r, c))
                        score += 1

        for c in range(N):
            if cols[c]:
                continue
            for r in range(N):
                if not rows[r]:
                    assert rows[r] is False
                    assert cols[c] is False
                    rows[r] = True
                    cols[c] = True
                    if bishops[r][c]:
                        pieces.append((QUEEN, r, c))
                        score += 1
                    else:
                        pieces.append((ROOK, r, c))
                        score += 1
                    break

        print "Case #%d: %d %d" % (t + 1, score, len(pieces))
        # assert score == N + N - 2
        for piece, r, c in pieces:
            print "%s %d %d" % (piece, r + 1, c + 1)
