import sys
import math
import string

def solve():
    N, R, O, Y, G, B, V = map(int, sys.stdin.readline().rstrip().split())

    oup = ''.join([x[1] for x in sorted([(R, 'R'), (Y, 'Y'), (B, 'B')])])
    inp = 'rby'
    trans = string.maketrans(inp, oup)

    R, B, Y = sorted([R, B, Y])



    if Y > N/2 or R + B < Y:
        return 'IMPOSSIBLE'

    s = B + R
    diff = math.ceil((s - Y)*1.0/2)
    diff = int(diff)
    Bred = B - diff
    Rred = R - diff

    assert Bred + Rred <= Y

    # Now reinsert diff * (BR) in the last section
    stable = ''
    if Bred > 0:
        stable += 'y' + 'y'.join(['b']*Bred)

    if Rred > 0:
        stable += 'y' + 'y'.join(['r']*Rred)

    if diff > 0:
        if Bred + Rred < Y:
            stable += 'y' + 'br'*diff
        elif stable[-1] == 'b':
            stable += 'rb'*diff
        else:
            stable += 'br'*diff

    assert stable.count('r') == R
    assert stable.count('b') == B
    assert stable.count('y') == Y

    return stable.translate(trans)

def main():
    T = int(sys.stdin.readline().rstrip())
    for t in range(1, T+1):
        answer = solve()
        print 'Case #{}: {}'.format(t, answer)

if __name__ == "__main__":
    main()
