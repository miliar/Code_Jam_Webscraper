import sys
import operator

def parse_pattern (pattern):
    tokens = []
    parens = False
    for c in pattern:
        if c == '(':
            parens = True
            tokens.append([])
        elif c == ')':
            parens = False
        else:
            if parens:
                tokens[-1].append(c)
            else:
                tokens.append(c)

    return tokens

if __name__ == '__main__':
    L, D, N = map(int, sys.stdin.readline().strip().split(" "))

    words = []
    for i in range(D):
        words.append(sys.stdin.readline().strip())

    for case in range(1, N+1):
        pattern = parse_pattern(sys.stdin.readline().strip())
        count = 0

        for word in words:
            count += sum(map(operator.contains, pattern, word)) == L
        print "Case #%d: %d" % (case, count)
